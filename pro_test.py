import numpy as np
import eko_rust
import time

# Create a huge grid (10 million points) to really stress the CPU
size = 10_000_000
x = np.linspace(0, 1, size)
y = x**2

#Test 1: Parallel Integration
start = time.time()
res = eko_rust.integrate_pdf_parallel(x, y)
print(f"Parallel Integration Result: {res:.6f} (Time: {(time.time()-start):.4f} s)")

#Test 2: Interpolation
# Find the value of x^2 at 0.5 (should be 0.25)
val = eko_rust.interpolate_x(0.5,x, y)
print(f"Interpolated value at x=0.5: {val:.4f})")