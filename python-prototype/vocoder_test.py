from phasevocoder import PhaseVocoder
import numpy as np
import matplotlib.pyplot as plt
import jsignal as jsig

# initialize the vocoder
w = 2 * np.pi * np.array([1000.])
fs = 20000.
pv = PhaseVocoder(w, fs)

# generate a test signal
fx = 1000.
t = 0.
tn = 2.
tot_time = tn - t0
t = np.linspace(t0, tn, int(fs * tot_time))
phi = 0.
A = 1.
x = A * np.cos(2 * np.pi * fx * t + phi)

# process the test signal with the vocoder
xhat = pv.process_signal(x, t)

# plot the results
plt.figure()
jsig.plt_time_and_mag(x, t, title='Original Signal')

plt.figure()
jsig.plt_time_and_mag(xhat, t, title='Processed Signal')

plt.show()