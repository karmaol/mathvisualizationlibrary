import matplotlib.pyplot as plt

def plot_bar(x, y, title=None, xlabel=None, ylabel=None, save_path=None):
    """Plot a bar graph."""
    plt.bar(x, y)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if title:
        plt.title(title)
    if save_path:
        plt.savefig(save_path)
    plt.show()
