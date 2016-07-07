import numpy as np
import matplotlib.pyplot as plt

def make_plots(filename):
    """Create a three-panel plot for the given dataset.
    
    Parameters
    ----------
    filename : str
        Filename for a CSV file giving inflammation data.
    
    Returns
    -------
    fig : Figure
        Three-panel plot showing mean, max, min inflammation
        across all patients for each day.
        
    """
    data = np.loadtxt(filename, delimiter=',')
    
    fig = plt.figure(figsize=(10, 3))

    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1, 3, 3)

    # plot the means
    ax1.set_ylabel('mean')
    ax1.plot(data.mean(axis=0))

    # plot the maxes
    ax2.set_ylabel('max')
    ax2.plot(data.max(axis=0))

    # plot the minses
    ax3.set_ylabel('min')
    ax3.plot(data.min(axis=0))

    fig.tight_layout()
    
    return fig

def identify_weirdness(filename):
    """Apply labeling to fishy datasets.
    
    Returns the label applied to the dataset.
    
    Parameters
    ----------
    filename : str
        Filename for a CSV file giving inflammation data.
        
    Returns
    -------
    label : str
        The flavor of fishiness of this data.
    
    """    
    data = np.loadtxt(filename, delimiter=',')
        
    if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:
        out = 'suspicious looking maxima!'
    elif data.min(axis=0).sum() == 0:
        out = 'minima add up to zero!'
    else:
        out = "seems okay!"
 
    return out

if __name__ == '__main__':

    import sys

    for filename in sys.argv[1:]:

        print(filename)

        # make and output a figure for the data to PDF
        fig = make_plots(filename)
        fig.savefig(filename + '.pdf')

        # give me the variety of weirdness the data displays
        print(identify_weirdness(filename))
