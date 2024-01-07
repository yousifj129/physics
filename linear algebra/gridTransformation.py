import numpy as np
import matplotlib.pyplot as plt
import time

def draw_grid(matrix, size, num_steps, delay):
    # Generate coordinates for the grid
    x = np.arange(0, size + 1)
    y = np.arange(0, size + 1)
    X, Y = np.meshgrid(x, y)

    # Define the initial transformation matrix
    initial_matrix = np.eye(2)

    # Calculate the incremental transformation matrix
    incremental_matrix = (matrix - initial_matrix) / num_steps

    # Create a figure and axis object
    fig, ax = plt.subplots()

    for i in range(num_steps + 1):
        # Calculate the intermediate transformation matrix
        intermediate_matrix = initial_matrix + i * incremental_matrix

        # Apply matrix transformation
        transformed_coords = np.matmul(intermediate_matrix, np.vstack([X.flatten(), Y.flatten()]))
        transformed_X = transformed_coords[0].reshape(X.shape)
        transformed_Y = transformed_coords[1].reshape(Y.shape)

        # Clear the previous plot
        ax.clear()

        # Plot the transformed grid
        ax.plot(transformed_X, transformed_Y, 'k-')
        ax.plot(transformed_X.T, transformed_Y.T, 'k-')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Grid Transformation')
        ax.grid(True)
        ax.axis('equal')

        # Draw the plot
        plt.draw()
        plt.pause(delay)
    plt.pause(10)

# Define the transformation matrix
matrix = np.array([[1, 3], [2, 1]])

# Define the size of the grid
size = 10

# Define the number of steps and delay between each step
num_steps = 100
delay = 0.05

# Draw the gradually transformed grid
draw_grid(matrix, size, num_steps, delay)