
# from sh_info import shInfoAbstract, _0_info
from sh_info import _0_info, _1_info, _2_info

def init_infos():
    '''Creates instance of each info and stores in dict'''
    infos = {}

    _0 = _0_info.Sh_0_info()
    infos[_0.id] = _0

    _1 = _1_info.Sh_1_info(_0.srs_gi['init_frames'])
    infos[_1.id] = _1

    _2 = _2_info.Sh_2_info(_0.srs_gi['init_frames'])
    infos[_2.id] = _2

    return infos