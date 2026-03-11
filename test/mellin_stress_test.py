import eko_rust
import numpy as np
import time

#Large grid
x= np.linspace(0, 100, 50000)
y = x**2 * (1-x)**3 # A more realistic PDF shape

# 500 Complex N-values along a contour (Real=2.0, Imag from -25 to 25)
n_values = [(2.0,i) for i in np.linspace(-25,25,500)]

print(f"--- Stress Testing 500 Complex Moments ---")
start = time.time()

# We call the Rust function 500 times
results = [eko_rust.mellin_moment(x, y, n_re, n_im) for n_re, n_im in n_values]

end = time.time()
print(f"Total time for 500 complex integrations: {end - start:.4f}s")
print(f"Average time per integration: {(end - start)/500:.6f}s")
print(f"First result sample: {results[0]}")