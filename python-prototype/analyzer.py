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
    def __init__(self, wn, bLowpass):
        self.wn = wn
        self.bLowpass = bLowpass

    def analyze(self, x, t):
        pass