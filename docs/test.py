from pyscript import window
import numpy as np

def hoge():
    print('ふが')
    print(window.aaa);
    
def f(param):
    return [ int(param[1]) * np.sin( 2*np.pi*int(param[2]) *i + 2*np.pi*int(param[3])/180 ) for i in range(int(param[0])) ]

def fft(x):
    return abs(np.fft.fft(x)).tolist()


__export__ = ['hoge', 'f', 'fft' ]
