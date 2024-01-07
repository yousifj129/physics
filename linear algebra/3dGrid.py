import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_3d_grid(matrix, size, num_steps, delay):
    # Generate coordinates for the grid
    x = np.arange(0, size + 1)
    y = np.arange(0, size + 1)
    z = np.arange(0, size + 1)

    X, Y, Z = np.meshgrid(x, y, z)

    points = np.array([X.flatten(), Y.flatten(), Z.flatten()])

    # Define the initial transformation matrix
    initial_matrix = np.eye(3)

    # Calculate the incremental transformation matrix
    incremental_matrix = (matrix - initial_matrix) / num_steps

    # Create a figure and axis object
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(num_steps + 1):
        # Calculate the intermediate transformation matrix
        intermediate_matrix = initial_matrix + i * incremental_matrix

        # Apply matrix transformation
        transformed_coords = np.matmul(intermediate_matrix, points)
        transformed_X = transformed_coords[0].reshape(X.shape)
        transformed_Y = transformed_coords[1].reshape(Y.shape)
        transformed_Z = transformed_coords[2].reshape(Z.shape)

        # Clear the previous plot
        ax.cla()

        # Plot the transformed grid
        ax.plot_surface(transformed_X, transformed_Y, transformed_Z, cmap='viridis')

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('3D Grid Transformation')

        # Set the aspect ratio
        ax.set_box_aspect([1, 1, 1])

        # Draw the plot
        plt.draw()
        plt.pause(delay)

# Define the transformation matrix
matrix = np.array([[2, 1, 0], [1, 2, 0], [0, 0, 1]])

# Define the size of the grid
size = 10

# Define the number of steps and delay between each step
num_steps = 100
delay = 0.05

# Draw the gradually transformed 3D grid
draw_3d_grid(matrix, size, num_steps, delay)