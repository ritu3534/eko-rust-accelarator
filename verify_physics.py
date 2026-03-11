import numpy as np
import eko_rust

# Create a grid of x values from 0 to 1
x = np.linspace(0, 1, 1000)
y = x**2

# Integrate in Rust (Integral of x^2 from 0 to 1 should be 1/3)
result = eko_rust.integrate_pdf(x, y)

print(f"--- EKO Physics Integration Test ---")
print(f"Rust Result:     {result:.6f}")
print(f"Analytical (1/3): 0.333333")

if np.isclose(result, 1/3, atol=1e-5):
    print("✅ SUCCESS: The Rust engine is accurate!")
else:
    print("❌ ERROR: Physics mismatch.")
