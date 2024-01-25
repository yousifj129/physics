from sympy import * 
def is_lorentz_invariant(tensor):
    v,c = symbols("v c")
    beta = v/c
    gamma = 1 / sqrt(1 - beta**2)
    
    # Create transformation matrix for Lorentz boost in the x direction
    boost_matrix = Matrix([[gamma, -gamma*beta, 0, 0],
                          [-gamma*beta, gamma, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])

    # Apply Lorentz boost to the tensor
    transformed_tensor =boost_matrix.T *tensor *boost_matrix

    # Simplify the transformed tensor
    simplified_tensor = simplify(transformed_tensor)
    print(simplified_tensor)
    print(tensor)
    # Check if the simplified tensor is equal to the original tensor
    return simplified_tensor == tensor

G, c ,m, r, theta = symbols('G c m r theta')
rs = 2*G*m/c**2
eta = Matrix([[-1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, r**2, 0],
              [0, 0, 0, r**2*sin(theta)**2]])

# Check if the Minkowski metric tensor is Lorentz invariant
result = is_lorentz_invariant(eta)

if result:
    print("The tensor is Lorentz invariant.")
else:
    print("The tensor is not Lorentz invariant.")