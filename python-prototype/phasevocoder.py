import numpy as np
from analyzer import Analyzer
from synthesizer import Synthesizer

class PhaseVocoder:
    # class constants
    #TODO: decide on filter parameters for the low-pass filter
    bLowpass = np.array([])

    # Constructor

    def __init__(self, w):
        # extract information from the input
        N = len(w)
        # initialize member variables
        self.initialize_analyzers(w, [self.bLowpass] * N)
        self.initialize_synthesizers(w)

    ### initialization methods

    def initialize_analyzers(self, w_list, bLowpass_list):
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
        if len(w_list) != len(bLowpass_list):
            raise ValueError('w_list and bLowpass_list must be the same '
                             'length')
        else:
            N = len(w_list)
        # initialize the analyzers
        analyzers = []
        for n in range(N):
            analyzers.append(Analyzer(w_list[n], bLowpass_list[n]))
        self.analyzers = analyzers

    def initialize_synthesizers(self, w_list):
        '''
        initialize_synthesizers(self, w_list): initializes each synthesizer
        in the vocoder based on the given center frequencies

        where
        w_list: a list of center frequencies for the desired synthesizers
        '''
        # initialize the synthesizers
        synthesizers = []
        for w in w_list:
            synthesizers.append(Synthesizer(w))
        self.synthesizers = synthesizers

    ### processing methods

    def process_signal(self, x, t, T):
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
        (mags, phases) = self.analyze(x, t, T)
        #TODO: detect the pitch of the incoming signal
        #TODO: calculate the necessary shift for the vocoder
        # synthesize a synthetic signal based on the analyzer outputs
        #TODO: feed the pitch shift information to the synthesizer
        return self.sythesize(t, mags, phases)

    def analyze(self, x, t, T):
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
            (mag, phase) = analyzer.analyze(x, t, T)
            mags.append(mag)
            phases.append(phase)
        return mags, phases

    def synthesize(self, t, mags, phases):
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
        x = np.zeros((t.size,))
        # iteratively add the harmonics from the analyzer
        for n in range(N):
            #TODO: feed the pitch shift information to the individual synthesizers
            x += self.synthesizers[n].synthesize(t, mags[n], phases[n])
        return x