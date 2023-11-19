import matplotlib.pyplot as plt

def plot_histogram(data, bins=None, title=None, xlabel=None, ylabel=None, save_path=None):
    """Plot a histogram."""
    plt.hist(data, bins=bins)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if title:
        plt.title(title)
    if save_path:
        plt.savefig(save_path)
    plt.show()
