import numpy as np
import sympy as sp
from itertools import product
from IPython.display import display

# Define the number of coordinates
n = 4

# Define the coordinate symbols
x = sp.symbols('t r theta phi')
G, c, M = sp.symbols('G c M')
r, theta, phi = sp.symbols('r theta phi')

# Define the covariant metric tensor using the Schwarzschild metric
covariant_metric = sp.Matrix([
    [-(1 - (2 * G * M) / (c ** 2 * r)), 0, 0, 0],
    [0, 1 / (1 - (2 * G * M) / (c ** 2 * r)), 0, 0],
    [0, 0, r ** 2, 0],
    [0, 0, 0, r ** 2 * sp.sin(theta) ** 2]
])

# Compute the contravariant metric tensor from the covariant metric tensor.
contravariant_metric = covariant_metric.inv()

# Display the covariant and contravariant metric tensors
print("Covariant Metric Components (g):")
display(covariant_metric)

print("Contravariant Metric Components (g^-1):")
display(contravariant_metric)

# Create array to store the symbolic notations of the Christoffel symbols.
gamma_list = np.zeros(shape=n, dtype='object')
christoffel_symbols = np.zeros(shape=(n, n, n), dtype='object')

for i in range(n):
    dummy_matrix = sp.zeros(n, n)
    for j, k, l in product(range(n), repeat=3):
        dummy_matrix[j, k] += (
            sp.Rational(1 / 2) * contravariant_metric[i, l] * (
                sp.diff(covariant_metric[l, j], x[k])
                + sp.diff(covariant_metric[l, k], x[j])
                - sp.diff(covariant_metric[j, k], x[l])
            )
        )
    gamma_list[i] = sp.simplify(dummy_matrix)

# Fill the christoffel_symbols array with the computed Christoffel symbols
for i, j, k in product(range(n), repeat=3):
    christoffel_symbols[i, j, k] = gamma_list[i][j, k]

# Display the Christoffel symbols for each dimension
for i in range(n):
    print(f"Christoffel Symbols for Dimension {x[i]}:")
    display(christoffel_symbols[i])
    print()