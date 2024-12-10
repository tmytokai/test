from pyscript import window

def hoge():
    print('ふが')
    print(window.aaa)
    window.aaa = 'piyo'
    

__export__ = ["hoge", ]
