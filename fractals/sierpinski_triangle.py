import numpy as np
import matplotlib.pyplot as plt

def generate_sierpinski_triangle(n_points, n_iterations):
    """Generate the Sierpinski triangle."""
    points = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, 0.5 * np.sqrt(3)]])
    result = np.zeros((n_points, 2))

    for _ in range(n_iterations):
        random_index = np.random.randint(3)
        result = (result + points[random_index]) / 2

    return result

def plot_sierpinski_triangle(n_points, n_iterations):
    """Plot the Sierpinski triangle."""
    points = generate_sierpinski_triangle(n_points, n_iterations)
    plt.scatter(points[:, 0], points[:, 1], s=1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sierpinski Triangle')
    plt.show()
