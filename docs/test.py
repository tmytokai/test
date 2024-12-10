from pyscript import sync

def hoge():
    print('ふが')
    print(sync.aaa)
    sync.bbb = 'hoge'
    

__export__ = ["hoge", ]
