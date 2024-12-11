from pyscript import window

def hoge(x):
    print('ふが')
    print(x);
    return 'piyo';
    
def fft(x):
    for i in x:
        print(i);
    return 'piyo';

__export__ = ['hoge', 'fft', ]
