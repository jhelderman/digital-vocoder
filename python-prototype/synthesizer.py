import numpy as np

class Synthesizer:
    #TODO: implement a pitch shifting operation
    '''
    synthesizer.py: a class that implements a synthesizer to reconstruct the 
    based on the output of the analyzer found in analyzer.py

    wn - the frequency that will be analyzed by this frequency analyzer
    '''
    def __init__(self, wn):
        self.wn = wn

    def synthesize(self, t, mag, phase):
        '''
        synthesize(self, t, mag, phase): a function that synthesizes a signal
        based on the output of the analyzer found in analyzer.py
            t: a one dimensional numpy array that represents the time values
               at which the resulting signal will be synthesized
          mag: a float representing the magnitude found using in analyzer.py
        phase: a float representing the phase found using analyzer.py
        '''
        return mag * np.cos(self.wn * t + phase)
        # return mag * np.cos(phase)