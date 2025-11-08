"""
Gradient Descent Algorithm in Python
------------------------------------
This program finds the local minima of the function:
    f(x) = (x + 3)^2
starting from a user-given initial point x₀.

Theory:
    Gradient descent update rule:
        x_new = x_old - η * f'(x_old)
where η is the learning rate (step size).

The true minimum of f(x) = (x + 3)^2 is at x = -3.
"""

import matplotlib.pyplot as plt

# Define the function f(x)
def f(x: float) -> float:
    return (x + 3) ** 2

# Derivative of f(x)
def df_dx(x: float) -> float:
    return 2 * (x + 3)

# ------------------------------
# Gradient Descent Implementation
# ------------------------------
curve = []

# User inputs
x_0 = float(input("Enter initial value for x (x₀): "))
n = int(input("Enter maximum number of steps (iterations): "))
step_size = float(input("Enter learning rate (step size): "))

# Store first point
curve.append((x_0, f(x_0)))

x_t = x_0
for i in range(n):
    grad = df_dx(x_t)
    x_t = x_t - step_size * grad  # update rule
    print(f"Step {i + 1:2d}: x = {x_t:.6f}, f(x) = {f(x_t):.6f}, gradient = {grad:.6f}")
    curve.append((x_t, f(x_t)))

print("\n---------------------------------")
print(f"Estimated local minimum at x = {x_t:.6f}")
print(f"Function value at minimum f(x) = {f(x_t):.6f}")
print("---------------------------------")

# ------------------------------
# Plotting convergence curve
# ------------------------------
x_vals, y_vals = zip(*curve)

plt.figure(figsize=(7, 4))
plt.plot(x_vals, y_vals, marker='o', color='blue', linestyle='-')
plt.title("Gradient Descent Convergence for f(x) = (x + 3)²")
plt.xlabel("x value")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
