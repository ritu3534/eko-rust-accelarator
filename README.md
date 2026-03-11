# EKO Rust Accelerator 🚀

A high-performance bridge between Python and Rust designed for PDF (Parton Distribution Function) evolution. This project demonstrates the "Oxidization" of numerical physics tools.

## 🌟 Key Features
* **21.6x Speedup:** Massive performance gain via true parallelism with Rust's `rayon` crate.
* **N-Space Physics:** Implementation of the **Mellin Transform** using `num-complex` for complex contour integration.
* **Numerical Precision:** Cubic/Cosine spline interpolation for smooth PDF sampling.
* **Zero-Copy Integration:** Seamless data sharing between Python/NumPy and Rust via `PyO3`.

## 📊 Performance Benchmark (20M Points)
| Method | Execution Time | Speedup |
| :--- | :--- | :--- |
| **NumPy (Standard)** | ~0.796s | 1.0x |
| **Rust (Oxidized)** | **~0.037s** | **21.6x** |

## 🛠 Tech Stack
* **Rust:** Ndarray, Rayon (Parallelism), Splines, Num-Complex.
* **Python:** NumPy, Matplotlib (Visualization).
* **Bridge:** PyO3 & Maturin.

## 🧪 Scientific Validation
The engine correctly calculates the 2nd Mellin Moment ($N=2$) for a toy PDF ($f(x) = x^2$):
* **Analytical Result:** 0.25000
* **Rust Engine Result:** 0.25000
