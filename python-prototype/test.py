import numpy as np
import scipy.signal as signal
import jsignal as jsig
import matplotlib.pyplot as plt

fs = 20000.
fc = 20.
dontcare_percent = 15.
fstop = fc * (1 + dontcare_percent)
fspec = np.array([0., fc, fstop, fs / 2.]) / fs
aspec = np.array([1., 0.])
ntaps = 401
firdelay = (ntaps - 1) / 2.

# get filter coefficients
b = signal.remez(ntaps, fspec, aspec)

# print design parameters
print 'Cutoff Frequency: {0} Hz'.format(fc)
print 'Stopband Frequency: {0} Hz'.format(fstop)
print 'FIR Filter Delay: {0} samples, {1} ms'.format(firdelay, firdelay / fs * 1000)

# plot frequency response
plt.figure()
jsig.plt_freqz(b)

plt.show()