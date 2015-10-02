import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import general_utilities as util


### signal transformations

def todb(x):
    return 20. * np.log(x)


def fromdb(x):
    return np.exp(x / 20.)


def magnitude_spectrum(x):
    return np.abs(np.fft.fft(x))


### plotting

def plt_magnitude_spectrum(x, db=True, fig=None, newfig=False, title=None):
    # switch figures
    hfig = util.initialize_plot(fig, newfig)
    # compute the magnitude spectrum
    X = magnitude_spectrum(x)
    if db:
        X = todb(X)
    # plot the magnitude spectrum
    f = np.linspace(0., 1., x.size)
    plt.plot(f, X)
    label_freq_domain()
    util.title_figure(title)
    return hfig


def plt_time_signal(x, t=None, fig=None, newfig=False, title=None):
    # parse arguments and set defaults
    if t == None:
        t = np.array(range(x.size))
    # initialize the plot
    hfig = util.initialize_plot(fig, newfig)
    # plot the time signal
    plt.plot(t, x)
    label_time_domain()
    util.title_figure(title)
    return hfig


def plt_time_and_mag(x, t=None, db=True, fig=None, newfig=False, title=None):
    # initialize the plot
    hfig = util.initialize_plot(fig, newfig)
    # plot the signal in the time domain
    plt.subplot(2,1,1)
    plt_time_signal(x, t, title=title)
    # plot the signal in the frequency domain
    plt.subplot(2,1,2)
    plt_magnitude_spectrum(x, db)
    plt.subplot(2,1,1)
    return hfig



def plt_freqz(b, a = 1, fig=None, title=None):
    """Plot the frequency response of a digital filter

    Inputs:
    b - transfer function denominator coefficients
    a - transfer function numerator coefficients
    Outputs:
    hfig - the figure on which the frequency response is plotted"""

    # switch figures
    hfig = util.switchfig(fig)
    # set defualts
    if title == None:
        title = 'Frequency Response'
    # calculate the frequency response
    w,H = signal.freqz(b, a)
    # adjust w so that the plot is on the interval [0, 0.5]
    w = w / (2 * np.pi)
    # generate the figure
    # plot the magnitude response
    plt.subplot(2,1,1)
    plt.plot(w, 20 * np.log(np.abs(H)))
    util.title_figure(title)
    label_freq_domain(y='Magnitude (dB)')
    # plot the phase response
    plt.subplot(2,1,2)
    plt.plot(w, np.angle(H))
    label_freq_domain(y='Angle (radians)')
    # return the figure
    return hfig


def label_time_domain(x='Time', y='Amplitude'):
    plt.xlabel(x)
    plt.ylabel(y)


def label_freq_domain(x='Normalized Frequency', y='Magnitude'):
    plt.xlabel(x)
    plt.ylabel(y)