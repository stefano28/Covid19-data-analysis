import matplotlib.pyplot as plt
from scipy import optimize
import numpy as n

def draw(stats, title, x_title, y_title):
    plt.title(title, fontsize=19)
    plt.xlabel(x_title, fontsize=10)
    plt.ylabel(y_title, fontsize=10)
    plt.scatter(stats['x'], stats['y'], s=10)
    plt.show()
