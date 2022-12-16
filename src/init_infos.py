
from sh_info import shInfoAbstract, _0_info

def init_infos(ch, PATH):
    '''Creates instance of each info and stores in dict'''
    infos = {}
    _n = _0_info.Sh_0_info()
    infos[_n.id] = _n

    return infos