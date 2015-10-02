import matplotlib.pyplot as plt

### plotting

def switchfig(fig=None):
    if fig == None:
        fig = plt.gcf()
    else:
        plt.figure(fig.number)
    return fig

def getnewfig(newfig=True):
    if newfig:
        fig = plt.figure()
    else:
        fig = None

def initialize_plot(fig=None, newfig=False):
    getnewfig(newfig)
    hfig = switchfig(fig)
    return hfig

def title_figure(title=None):
    if title != None:
        plt.title(title)