import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import jsignal as jsig

# parameters
fn = 1000.0
wn = 2 * np.pi * fn
w = wn
fs = 44100.0
t0 = 0
tEnd = 2 * np.pi / wn
nPts = round((tEnd - t0) * fs)
t = np.linspace(t0, tEnd, nPts)

# calculate test signal
x = np.cos(w * t)

# calculate oscillators
qosc = np.sin(wn * t)
iosc = np.cos(wn * t)

# calculate lowpass filter coeffiecients
n = 100
fc = 20.0
cutoff = fc / fs
b = signal.firwin(n, cutoff, window = 'hamming')

# modulate the test signal
xmodi = iosc * x
xmodq = qosc * x

# lowpass filter the modulated signal
lpmodi = signal.lfilter(b, 1, xmodi)
lpmodq = signal.lfilter(b, 1, xmodq)

# display results


# plot results
plt.figure()
plt.stem(t, iosc)
jsig.pltmagspect(xmodi)
jsig.pltfreqz(b)
jsig.pltmagspect(lpmodi)
plt.show()