import numpy as np

def f(N):
    return [ 2*np.sin(2*np.pi/4*i)+3*np.cos(2*np.pi/8*i) for i in range(int(N)) ]

def g(N):
    return [ -i for i in range(int(N)) ]

def powerspectrum(x):
    return (np.abs(np.fft.fft(x))**2).tolist()

__export__ = ['f', 'g', 'powerspectrum']
