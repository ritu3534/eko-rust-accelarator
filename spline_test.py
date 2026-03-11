import numpy as np
import eko_rust

# Small grid for testing
x = np.array([0.0, 1.0, 2.0])
y = np.array([0.0, 1.0, 0.0]) # A simple "mountain" shape

# Evaluate at 0.25 (where the curve difference is visible)
val_linear = 0.25 
val_spline = eko_rust.spline_interpolate(0.25, x, y)

print(f"--- Physics Curve Test at x=0.25 ---")
print(f"Linear (Sharp): {val_linear}")
print(f"Spline (Smooth): {val_spline:.4f}")

if val_spline > val_linear:
    print("✅ The Spline is creating a smooth 'arch' above the linear line!")
