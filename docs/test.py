from pyscript import window
import numpy as np

def hoge():
    print('ふが')
    print(window.aaa);
    
def fft(x):
    for i in x:
        print(i);
    y = np.fft.fft(x)
    print(y)
    return abs(y)

__export__ = ['hoge', 'fft', ]
