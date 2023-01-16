
import random

import P

# from sh_info import shInfoAbstract, _0_info
from sh_info import _0_info, _1_info, _2_info

def init_infos():
    '''Creates instance of each info and stores in dict'''
    infos = {}

    pulse = random.sample(range(1, 200), 20)
    pulse.sort()

    _0 = _0_info.Sh_0_info(pulse)
    infos[_0.id] = _0

    if '1' in P.SHS_TO_SHOW:
        _1 = _1_info.Sh_1_info(pulse)
        infos[_1.id] = _1

    if '2' in P.SHS_TO_SHOW:
        _2 = _2_info.Sh_2_info(pulse)
        infos[_2.id] = _2

    return infos