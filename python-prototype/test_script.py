import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import jsignal as jsig

nPts = 1000
fn = 1000.0
wn = 2 * np.pi * fn
fs = 44100.0
fc = 20.0
cutoff = fc / fs
n = 100
t = np.linspace(0, 2*np.pi, nPts)
sinosc = np.sin(wn * t)
cososc = np.cos(wn * t)
b = signal.firwin(n, cutoff, window = 'hamming')
jsig.pltfreqz(b)
plt.show()