import numpy as np
import matplotlib.pyplot as plt

def generate_julia_set(width, height, xmin, xmax, ymin, ymax, max_iter, c):
    """Generate a Julia set."""
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    z = X + 1j * Y
    img = np.zeros((height, width))

    for i in range(max_iter):
        mask = np.abs(z) < 10
        z[mask] = z[mask] * z[mask] + c
        img += mask

    return img

def plot_julia_set(width, height, xmin, xmax, ymin, ymax, max_iter, c):
    """Plot a Julia set."""
    img = generate_julia_set(width, height, xmin, xmax, ymin, ymax, max_iter, c)
    plt.imshow(img.T, cmap='hot', extent=[xmin, xmax, ymin, ymax])
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.title(f'Julia Set (c = {c})')
    plt.show()
