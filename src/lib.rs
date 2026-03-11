use pyo3::prelude::*;
use numpy::{PyReadonlyArray1, PyReadonlyArray2,PyArray1,ToPyArray};
use ndarray::Array1;
use ndarray::prelude::*;
use rayon::prelude::*;
use splines::{Interpolation, Key ,Spline}; // Spline Engine
use num_complex::{Complex64,ComplexFloat};

// PARALLEL INTEGRATION USING RAYON
#[pyfunction]
fn integrate_pdf_parallel(x_grid: PyReadonlyArray1<f64>, y_grid: PyReadonlyArray1<f64>) -> PyResult<f64> {
    let x = x_grid.as_array();
    let y = y_grid.as_array();

    if x.len() != y.len() || x.len() < 2 {
        return Ok(0.0);
    }
    // rayon splits the loop across all CPU cores automatically
    let total: f64 = (0..x.len() - 1)
        .into_par_iter()
        .map(|i| 0.5 * (y[i] + y[i+1]) * (x[i+1] - x[i]))
        .sum();
    
    Ok(total)
}
// 2.PARALLEL INTERPOLATION USING RAYON(CUBIC SPLINE INTERPOLATOR)
// Mathematically: y = y0 + (x - x0) * ((y1 - y0) / (x1 - x0))
#[pyfunction]
fn spline_interpolate(x_val: f64, x_grid: PyReadonlyArray1<f64>, y_grid: PyReadonlyArray1<f64>) -> PyResult<f64> {
    let x = x_grid.as_array();
    let y = y_grid.as_array();
   // Create keys for the spline engine
   let keys: Vec<Key<f64,f64>> = x.iter()
     .zip(y.iter())
     .map(|(&xi, &yi)| Key::new(xi,yi,Interpolation::Cosine))
     .collect();

   let spline = Spline::from_vec(keys);

   // Sample the spline at x_val
    Ok(spline.sample(x_val).unwrap_or(0.0))
}
// 3.PARALLEL EVOLUTION KERNEL APPLICATION
#[pyfunction]
fn apply_evolution_kernel(
    kernel: PyReadonlyArray2<f64>, pdf_values: PyReadonlyArray1<f64>) -> PyResult<Py<PyArray1<f64>>> {
    // 1.Convert the Python inputs to Rust ndarray view (zero-copy!)
    let k = kernel.as_array();
    let f = pdf_values.as_array();
    
    let result : Array1<f64> =k.dot(&f);
    // Return the result back to python as a Numpy array
    Python::with_gil(|py| { Ok(result.to_pyarray(py).unbind()) })
    }

    // --- 4. MELLIN TRANSFORM (N-SPACE) ---
#[pyfunction]
fn mellin_moment(x_grid: PyReadonlyArray1<f64>, y_grid: PyReadonlyArray1<f64>, n_real: f64, n_imag: f64) -> PyResult<(f64, f64)> {
    let x = x_grid.as_array();
    let y = y_grid.as_array();

    // Create the complex N value: N= real + i*imag
    let n = Complex64::new(n_real, n_imag);

    // Parallel integration of : Integral [ f(x) * x^(n-1) dx ] using the midpoint rule
    let result: Complex64 = (0..x.len() - 1)
        .into_par_iter()
        .map(|i| {
            let x_mid = (x[i] + x[i+1]) / 2.0;
            let y_mid = (y[i] + y[i+1]) / 2.0;
            let dx = x[i+1] - x[i];

            // We convert the real values to Complex64 before math 
            // to ensure powc and sum work correctly.
            // Complex math: y * x^(n-1) * dx
            let weight = Complex64::from(x_mid).powc(n - 1.0);
            Complex64::from(y_mid) * weight * dx
    
        })
        .sum();
        // Return as a tuple of (real, imag) since Python handles tuples easily 
    Ok((result.re, result.im))
}

#[pymodule]
fn eko_rust(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(integrate_pdf_parallel, m)?)?;
    m.add_function(wrap_pyfunction!(apply_evolution_kernel, m)?)?;
    m.add_function(wrap_pyfunction!(spline_interpolate, m)?)?;
    m.add_function(wrap_pyfunction!(mellin_moment, m)?)?;
    Ok(())
}