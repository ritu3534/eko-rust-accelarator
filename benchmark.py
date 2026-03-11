import numpy as np
import eko_rust
import time

# 1.Create a massive grid (20 million points)
# This would normally crawl in pure Python
size = 20_000_000
x = np.linspace(0.01, 1.0, size)
y = np.exp(-x) * np.sin(x)# complex function to integrate

print(f"--- Benchmarking {size:,} points ---")

# 2. Python/Numpy Baseline
start_py = time.time()
if hasattr(np, 'trapezoid'):
    py_result = np.trapezoid(y, x)  # Modern NumPy 2.0+
else:
   py_result = np.trapz(y, x)
end_py = time.time()
print(f"NumPy Time: {(end_py - start_py):.4f}s")

# 3. Rust Parallel Engine
start_rs = time.time()
rs_result = eko_rust.integrate_pdf_parallel(x, y)
end_rs = time.time()
print(f"Rust Parallel Time: {(end_rs - start_rs):.4f}s")


# 4. result
speedup =(end_py - start_py)/ (end_rs - start_rs)
print(f"\n Result Match : {np.isclose(py_result, rs_result,)}")
print(f"🚀 Rust is {speedup:.2f}x faster than NumPy/Python!")