import sympy


x, y, z = sympy.symbols('x y z')

M = sympy.Matrix([[1, 2], [3, 4]])
determinant = M.det()
print(determinant)