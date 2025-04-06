# visualization.py

import matplotlib.pyplot as plt
import numpy as np
import config

def plot_population(population, alpha, generation, save_path=None, show_plot=True):
    """
    Rysuje populację w 2D wraz z optymalnym fenotypem alpha.
    Można zarówno wyświetlać (show_plot=True),
    jak i zapisywać obraz (save_path != None).
    """
    x = [ind.get_phenotype()[0] for ind in population]
    y = [ind.get_phenotype()[1] for ind in population]
    
    plt.figure(figsize=(5, 5))
    plt.scatter(x, y, label="Populacja", alpha=0.1)
    plt.scatter([alpha[0]], [alpha[1]], color='red', label="Optimum", marker='X')
    plt.title(f"Pokolenie: {generation}")
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.legend()
    plt.tight_layout()
    
    if save_path is not None:
        plt.savefig(save_path)  # Zapis do pliku
    if show_plot:
        plt.show()
    else:
        # Jeśli nie chcesz pokazywać, to zamykaj figurę, 
        # żeby nie zapełniać pamięci
        plt.close()

def plot_phys_space(population, generation, save_path=None, show_plot=True):

    x = [ind.get_coordinates()[1] for ind in population]
    y = [ind.get_coordinates()[0] for ind in population]

    plt.figure(figsize=(10, 5))
    plt.scatter(x, y, label="Populacja", alpha=0.1)

    #plt.xticks(np.arange(0, 28, 1))
    #plt.yticks(np.arange(0, 14, 1))

    plt.xticks(np.arange(0, config.plate_length+1, 1))
    plt.yticks(np.arange(0, config.plate_width+1, 1))

    plt.grid(True, linestyle = "--", color = "gray", linewidth=0.5, alpha = 0.7)

    for x_line in np.arange(0, config.plate_length + 1, 3):
        plt.axvline(x_line, color="red", linestyle="-", linewidth=1)

    plt.title(f"Pokolenie: {generation}")
    plt.xlim(0, config.plate_length)
    plt.ylim(0, config.plate_width)
    plt.legend()
    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path)  # Zapis do pliku
    if show_plot:
        plt.show()
    else:
        # Jeśli nie chcesz pokazywać, to zamykaj figurę,
        # żeby nie zapełniać pamięci
        plt.close()

def plot_bars(quants, title, xlabel, ylabel, filename, categories):

    plt.bar(categories, [q[0] for q in quants])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.savefig(filename)

def plot_lines(quants, title, xlabel, ylabel, filename, categories):


    time = range(len(quants[0]))

    for i, l in enumerate(quants):
        plt.plot(time, l, marker='.', label = categories[i])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.savefig(filename)

def plot_line(quants, title, xlabel, ylabel, filename):


    time = range(len(quants))


    plt.plot(time, quants, marker='.')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.savefig(filename)
