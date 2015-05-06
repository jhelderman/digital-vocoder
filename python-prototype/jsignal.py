import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def pltfreqz(b, a = 1):
    w,H = signal.freqz(b, a)
    w = w / (2 * np.pi)
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.plot(w, 20 * np.log(np.abs(H)))
    plt.title('Frequency Response')
    plt.xlabel('Normalized Frequency')
    plt.ylabel('Magnitude (dB)')
    plt.subplot(2,1,2)
    plt.plot(w, np.angle(H))
    plt.xlabel('Normalized Frequency')
    plt.ylabel('Angle (radians)')