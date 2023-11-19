import numpy as np
import matplotlib.pyplot as plt

def generate_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    """Generate the Mandelbrot set."""
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y
    z = np.zeros_like(c)
    img = np.zeros((height, width))

    for i in range(max_iter):
        mask = np.abs(z) < 10
        z[mask] = z[mask] * z[mask] + c[mask]
        img += mask

    return img

def plot_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter):
    """Plot the Mandelbrot set."""
    img = generate_mandelbrot(width, height, xmin, xmax, ymin, ymax, max_iter)
    plt.imshow(img.T, cmap='hot', extent=[xmin, xmax, ymin, ymax])
    plt.xlabel('Re(c)')
    plt.ylabel('Im(c)')
    plt.title('Mandelbrot Set')
    plt.show()
