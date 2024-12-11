from pyscript import window
import numpy as np

def hoge():
    print('ふが')
    print(window.aaa);
    
def fft(x,y):
    for i in x:
        print(i);
    y = abs(np.fft.fft(x))
    print(y)

__export__ = ['hoge', 'fft', ]
