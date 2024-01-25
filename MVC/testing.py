import numpy as np
import matplotlib.pyplot as plt

# Define the vector-valued position function
def f(xy):
    x, y = xy
    return np.array([x + np.sin(y), y + np.sin(x)])

# Generate grid points for x and y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Evaluate the position function at each grid point
Z = f([X, Y])

# Plot the curves
plt.contour(X, Y, Z[0], levels=100, cmap='viridis')
plt.contour(X, Y, Z[1], levels=100, cmap='plasma')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Vector-valued Position Function')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)
plt.colorbar(label='Curve Values')
plt.show()