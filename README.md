# EKO Rust Accelerator 🚀
**GSoC 2026 Proof-of-Concept | Target: CERN/HSF - NNPDF**

This repository serves as a technical Proof-of-Concept for the "Oxidizing EKO" project. It demonstrates the acceleration of numerical kernels for DGLAP evolution using Rust, while maintaining a seamless Python interface via PyO3 and Maturin.

## 🚀 Performance Benchmarks
Comparison of PDF integration on a grid of **20 million points**.

| Method | Execution Time | Speedup |
| :--- | :--- | :--- |
| **NumPy (Standard)** | ~0.796s | 1.0x |
| **Rust (Oxidized)** | **~0.037s** | **21.6x** |

> **Note:** Benchmarks were performed on an x86_64 Linux environment. Accuracy was verified against the legacy Python implementation with a residual error of $< 10^{-12}$.

## 🧪 Physics Overview: Mellin Inversion
The core of EKO involves solving the DGLAP equations by turning integro-differential equations into a linear algebra problem. This PoC implements:
* **Talbot-contour integration:** A robust method for the numerical inversion of the Mellin transform using a deformed path in the complex plane.
* **Complex Arithmetic:** Utilizing `num-complex` to handle the N-space evolution operators and complex power-law kernels.



## ✅ Accuracy & Validation
Numerical results for the 2nd Mellin Moment of $f(x) = x^2$:
* **Analytical Result:** 0.250000000000
* **Rust PoC Result:** 0.250000000000
* **Precision:** Double-precision float (f64) matching standard theory benchmarks.

## 🛠 Tech Stack
* **Language:** Rust (Core Numerical Kernels)
* **Interop:** PyO3 & Maturin (Python FFI)
* **Parallelism:** Rayon (Data-parallelism via work-stealing)
* **Math:** `ndarray` for memory-efficient handling and `num-complex` for N-space.

## 🏗 Project Structure
```text
├── .github/workflows/  <-- Automated CI/CD Testing
├── src/
│   └── lib.rs          <-- Rust Kernels (Integrators, Splines, Mellin)
├── Cargo.toml          <-- Rust Dependencies
├── benchmark.py        <-- Performance Validation
├── test_mellin.py      <-- Physics Validation
└── README.md
```
