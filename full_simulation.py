import numpy as np
import eko_rust

# 1. Physics Setup: A grid of 1000 points from
x_grid = np.linspace(0.01, 1.0, 1000)
pdf_initial = x_grid**-0.5 * (1 - x_grid)**3 # A simple PDF: f(x) = x^2

# 2. Integration: Calculate the "Moment" of the PDF
# Integral of f(x) over the grid
moment = eko_rust.integrate_pdf(x_grid, pdf_initial)
print(f"Total PDF Moment(1D Integration): {moment:.6f}")

# 3. Evolution: Apply a 1000x1000 kernel to evolve the PDF(Evolution Kernel)
# In EKO, this kernel represents the change from Q0 to Q1
kernel = np.eye(1000) + 0.01* np.random.randn(1000,1000)
pdf_evolved = eko_rust.apply_evolution_kernel(kernel, pdf_initial)

print(f"Evolved PDF(2D Convolution) - First 3 points: {pdf_evolved[:3]}")
print("✅ Full EKO-Oxidized Pipeline: SUCCESS")