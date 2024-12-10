from pyscript import sync

def hoge(aaa):
    print('ふが')
    sync.aaa = 'hoge'
    

__export__ = ["hoge", ]
