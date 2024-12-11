from pyscript import window
import numpy as np

def hoge():
    print('ふが')
    print(window.aaa);
    
def fft(x):
    for i in x:
        print(i);
    y = abs(np.fft.fft(x))
    print(y)
    return y

__export__ = ['hoge', 'fft', ]
