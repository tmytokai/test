import numpy as np

def f(parameter):
    N = int(parameter[0])
    return [ 2*np.sin(2*np.pi/4*i)+3*np.cos(2*np.pi/8*i) for i in range(N) ]

def fft(x):
    return abs(np.fft.fft(x)).tolist()


__export__ = ['f', 'fft']
