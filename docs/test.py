from pyscript import window
import numpy as np

def hoge():
    print('fugafuga')
    print(window.aaa);
    
def f(param):
    return [ int(param[1]) * np.sin( 2*np.pi*int(param[2]) *i + 2*np.pi*int(param[3])/180 ) for i in range(int(param[0])) ]

def sin(param):
    A = float(param[0])
    w = 2*np.pi*float(param[1])
    t = float(param[2])
    psi = 2*np.pi*float(param[3])/180
    return [A*np.sin( w*t + psi )]

def fft(x):
    return abs(np.fft.fft(x)).tolist()


__export__ = ['hoge', 'f', 'sin', 'fft' ]
