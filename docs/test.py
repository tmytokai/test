from pyscript import window

def hoge():
    print('ふが')
    print(sync.aaa)
    sync.bbb = 'hoge'
    

__export__ = ["hoge", ]
