import numpy as np
from scipy import signal

class Analyzer:
    """
    Analyzer.py: A class implementing a version of the STFT analyzer described 
    in "Phase Vocoder" by Flanagan and Golden. This analyzer will be used in the
    analysis-synthesis procedure used in the implementation of a digital phase
    vocoder. The class contains and maintains the following data.

          wn - the frequency that will be analyzed by this frequency analyzer
    bLowpass - the filter coeficients for the lowpass filter used in the 
               implemntation of this analyzer
    """
    bdiff = np.array([1, -1])

    def __init__(self, wn, bLowpass):
        self.wn = float(wn)
        self.bLowpass = bLowpass

    def analyze(self, x, t, T):
        '''
        analyze(self, x, t, T): analyze the given signal using the procedure 
        outlined in "Phase Vocoder" by Flanagan and Golden

        where
        x: a one dimensional numpy array that represents the given signal
        t: a one dimensional numpy array of the same size as x that 
           represents the time values at which the samples of x were taken
        '''
        # check to make sure x and t are the same size
        if x.size != t.size:
            raise ValueError('x and t must be the same size')
        # generate the local oscillators
        qlo = np.sin(self.wn * t)
        ilo = np.cos(self.wn * t)
        # modulate the input signal
        xmodq = x * qlo
        xmodi = x * ilo
        # lowpass filter the modulated signal
        a = signal.lfilter(bLowpass, 1, xmodi)
        b = signal.lfilter(bLowpass, 1, xmodq)
        # calculate delta a and delta b using a derivative filter
        da = signal.lfilter(bdiff, 1, xmodi)
        db = signal.lfilter(bdiff, 1, xmodq)
        # estimate the magnitude spectrum at wn
        mag = np.sqrt(a ** 2 + b ** 2)
        # estimate the phase spectrum at wn
        phase = (b * da - a * db) / (T * (a ** 2 + b ** 2))
        # return the magnitude, phase tuple
        return mag, phase