
import random

import P

# from sh_info import shInfoAbstract, _0_info
from sh_info import _0_info, _1_info, _2_info, _3_info, _4_info, _5_info

def init_infos():
    '''Creates instance of each info and stores in dict'''
    infos = {}

    top_point0 = [210, 70]
    top_point1 = [210, 90]  # aft expl
    top_point2 = [210, 90]  # for 3 rocks

    pulse_sr1 = random.sample(range(1, 200), 30)  # 1 (sr)
    pulse_0 = random.sample(range(20, 300), 5)  # 0 after initial srs
    pulse_c3 = random.sample(range(300, 450), 20)  # expl

    pulse_0.sort()
    pulse_sr1.sort()
    pulse_c3.sort()

    if '0' in P.SHS_TO_SHOW:  # BEF EXPL
        _0 = _0_info.Sh_0_info(pulse_0, top_point0)
        infos[_0.id] = _0

    if '1' in P.SHS_TO_SHOW:  # ALL OF THEM. LD NEEDS TO WORK FOR BOTH
        _1 = _1_info.Sh_1_info(pulse_sr1, top_point1)
        infos[_1.id] = _1

    if '2' in P.SHS_TO_SHOW:  # DOWN LEFT
        _2 = _2_info.Sh_2_info(pulse_sr1, top_point0)
        infos[_2.id] = _2

    if '3' in P.SHS_TO_SHOW and P.A_CS:  # ROCKS
        _3 = _3_info.Sh_3_info(pulse_c3, top_point2)
        infos[_3.id] = _3

    # 4: # DOWN RIGHT

    # 5: 0 but after expl
    if '5' in P.SHS_TO_SHOW:  # BEF EXPL
        _5 = _5_info.Sh_5_info(pulse, top_point0)
        infos[_5.id] = _5

    return infos