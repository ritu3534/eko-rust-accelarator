import eko_rust
import numpy as np

x = np.linspace(0.01, 1.0, 1000)
y = x**2 # simple PDF

# Calculate the 2nd moment (n=2 + 0j)
# Integral of x^(2-1) * x^2 = integral x^3 dx =1/4 = 0.25
real,imag = eko_rust.mellin_moment(x,y,2.0,0.0)

print(f"Mellin Moment (N=2): {real:.5f} + {imag:.5f}i")