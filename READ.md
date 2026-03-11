# EKO Rust Accelerator 🚀

A high-performance bridge between Python and Rust designed for PDF (Parton Distribution Function) evolution.

## Key Features
* **21x Speedup:** Parallelized numerical integration using Rust's `Rayon` crate.
* **N-Space Physics:** Implementation of the Mellin Transform using `num-complex` for complex contour integration.
* **Oxidized Architecture:** Seamless Python-Rust integration via `PyO3` and `maturin`.
* **Numerical Precision:** Cubic spline interpolation for smooth PDF grid sampling.

## Performance Benchmark
* **NumPy (Standard):** 0.79s
* **Rust (Oxidized):** 0.03s
* **Result:** ~21.6x faster than native Python/NumPy for large-scale PDF grids.