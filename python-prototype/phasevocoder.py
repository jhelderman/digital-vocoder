import numpy as np
import scipy.signal as signal
from analyzer import Analyzer
from synthesizer import Synthesizer

class PhaseVocoder:
    # default class members
    ntaps = 401  # number of low-pass filter taps
    fc = 20.0  # cutoff frequency of the filter in Hz
    fs = 44100.

    # Constructor

    def __init__(self, w, fs=None):
        # extract information from the input
        N = w.size
        # sampling frequency
        if fs != None:
            self.fs = fs
        # get the filter coefficients
        cutoff = self.fc / self.fs
        percent_transition = 15.
        fstop = cutoff * (1 + percent_transition)
        # self.bLowpass = signal.firwin(self.ntaps, cutoff, window = 'hamming')
        fspec = [0., cutoff, fstop, 0.5]
        aspec = [1., 0.]
        self.bLowpass = signal.remez(self.ntaps, fspec, aspec)
        # initialize member variables
        self.initialize_analyzers(w, [self.bLowpass] * N)
        self.initialize_synthesizers(w)

    ### initialization methods

    def initialize_analyzers(self, w, bLowpass_list):
        '''
        initialize_analyzers(self, w_list, bLowpass_list): initialize each
        analyzer in the vocoder based on the given center frequencies and 
        low-pass filter coefficients

        where
               w_list: a list of center frequencies for the desired analyzers
        bLowpass_list: a list of the same length as w_list that contains numpy
                       arrays with low-pass filter coefficients for the 
                       analyzers
        '''
        # validate the inputs
        if w.size != len(bLowpass_list):
            raise ValueError('w_list and bLowpass_list must be the same '
                             'length')
        else:
            N = w.size
        # initialize the analyzers
        analyzers = []
        for n in range(N):
            analyzers.append(Analyzer(w[n], bLowpass_list[n]))
        self.analyzers = analyzers

    def initialize_synthesizers(self, w):
        '''
        initialize_synthesizers(self, w_list): initializes each synthesizer
        in the vocoder based on the given center frequencies

        where
        w_list: a list of center frequencies for the desired synthesizers
        '''
        # initialize the synthesizers
        synthesizers = []
        for wp in np.nditer(w):
            synthesizers.append(Synthesizer(wp))
        self.synthesizers = synthesizers

    ### processing methods

    def process_signal(self, x, t):
        '''
        process_signal(self, x, t, T): processes a single signal using the
        phase vocoder analysis/synthesis procedure

        where
        x: a one-dimensional numpy array representing the signal to be analyzed
        t: a one-dimensional numpy array, of the same size as x, representing
           the time values at which x was sampled
        T:
        '''
        # analyze the signal
        (mags, phases) = self.analyze(x, t)
        #TODO: detect the pitch of the incoming signal
        #TODO: calculate the necessary shift for the vocoder
        # synthesize a synthetic signal based on the analyzer outputs
        #TODO: feed the pitch shift information to the synthesizer
        return self.synthesize(t, mags, phases)

    def analyze(self, x, t):
        '''
        analyze(self, x, t, T): analyzes the incoming signal with the 
        analyzers defined during the instantiation of the given instance

        where
        x: a one-dimensional numpy array representing the signal to be analyzed
        t: a one-dimensional numpy array, of the same size as x, representing
           the time values at which x was sampled
        T:
        '''
        # calculate the output of each analyzer
        mags = []
        phases = []
        for analyzer in self.analyzers:
            (mag, phase) = analyzer.analyze(x, t)
            mags.append(mag)
            phases.append(phase)
        return mags, phases

    def synthesize(self, t,  mags, phases):
        '''
        synthesize(self, t, mags, phases): synthesizes a signal based on given
        analyzer outputs and the synthesizers defined for the given instance

        where
             t: a one-dimensional numpy array, of the same size as x, 
                representing
          mags: a list of floats representing the magnitudes calculated by the 
                analyzers
        phases: a list of floats representing the phases calculated by the 
                synthesizers
        '''
        # validate the inputs
        if len(mags) != len(phases):
            raise ValueError('mags and phases must be the same length')
        elif len(mags) != len(self.synthesizers):
            raise ValueError('mags and phases must have a value for every synthesizer')
        else:
            N = len(mags)
        # initialize the signal vector
        x = np.zeros((mags[0].size,))
        # iteratively add the harmonics from the analyzer
        for n in range(N):
            #TODO: feed the pitch shift information to the individual synthesizers
            x += self.synthesizers[n].synthesize(t, mags[n], phases[n])
        return x