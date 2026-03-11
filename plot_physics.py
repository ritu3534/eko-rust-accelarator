import numpy as np
import eko_rust
import matplotlib.pyplot as plt

# 1. Define the sparse grid(only 3 points)
x_grid =np.array([0.0, 1.0, 2.0])
y_grid = np.array([0.0, 1.0, 0.0]) # A simple "mountain" shape

# 2. Create a dense set of points to "probe" the curve
x_dense = np.linspace(0, 2, 100)

# 3. Calculate values using our Rust spline interpolation
y_spline =[eko_rust.spline_interpolate(val, x_grid, y_grid) for val in x_dense]

# 4. Calculate the linear values for comparison
y_spline = [eko_rust.spline_interpolate(val, x_grid, y_grid) for val in x_dense]


# 5. Plotting
plt.figure(figsize=(8, 5))
plt.plot(x_dense, y_spline, label= 'Original Grid Points')
plt.plot(x_dense, x_dense if x_dense.all() < 1 else np.where(x_dense < 1, x_dense, 2-x_dense), '--', alpha=0.3, label='Linear path')
plt.plot(x_dense, y_spline, 'b-', label='Rust Spline (Oxidized)')

plt.title("EKO PDF Interpolation - Linear vs Spline",fontsize=14)
plt.xlabel("x(Momentum Fraction)",fontsize=12)
plt.ylabel("f(x) (PDF Value)",fontsize=12)
plt.legend()
plt.grid(True,linestyle=':',alpha=0.7)

print("Generating plot...")
plt.savefig("physics_curve.png")
print("✅ Success! Open 'physics_curve.png' to see your Oxidized Spline.")