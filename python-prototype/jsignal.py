import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def pltfreqz(b, a = 1):
    """Plot the frequency of a digital filter

    Inputs:
    b - transfer function denominator coefficients
    a - transfer function numerator coefficients
    Outputs:
    hfig - the figure on which the frequency response is plotted"""

    # calculate the frequency response
    w,H = signal.freqz(b, a)

    # adjust w so that the plot is on the interval [0, 0.5]
    w = w / (2 * np.pi)

    # generate the figure
    hfig = plt.figure()

    # plot the magnitude response
    plt.subplot(2,1,1)
    plt.plot(w, 20 * np.log(np.abs(H)))
    plt.title('Frequency Response')
    plt.xlabel('Normalized Frequency')
    plt.ylabel('Magnitude (dB)')

    # plot the phase response
    plt.subplot(2,1,2)
    plt.plot(w, np.angle(H))
    plt.xlabel('Normalized Frequency')
    plt.ylabel('Angle (radians)')

    # return the figure
    return hfig

def pltmagspect(x):
    hfig = plt.figure()
    plt.plot(np.linspace(0, 1, len(x)), np.log10(np.abs(np.fft.fft(x))))
    plt.xlabel('Normalized Frequency')
    plt.ylabel('Magnitude (dB)')
    return hfig