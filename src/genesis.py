
import random

import P

# from sh_info import shInfoAbstract, _0_info
from sh_info import _0_info, _1_info, _2_info, _3_info, _4_info, _5_info, _6_info

def init_infos():
    '''Creates instance of each info and stores in dict'''
    infos = {}

    top_point0 = [210, 70]
    top_point1 = [210, 90]  # aft expl
    top_point2 = [210, 90]  # for 3 rocks

    pulse_sr1 = random.sample(range(5, 500), 50)  # 1 (sr)  # OBS '2' CAN ONLY BE TESTED WHEN STARTS AT 100
    # pulse_sr1 = [110, 150]  # 1 (sr)
    pulse_0 = random.sample(range(50, 300), 15)  # 0 after initial srs
    # pulse_0 = [50, 250]
    pulse_2 = [110, 180]  # sps uses -100 OBS MAY GET WRONG
    pulse_c3 = random.sample(range(150, 450), 30)  # expl
    # pulse_c3 = [10, 50, 100]  # expl
    # pulse_c3 = random.sample(range(100, 200), 10)  # post expl
    pulse_5 = random.sample(range(200, 500), 20)  # post expl
    # pulse_5 = random.sample(range(5, 200), 10)  # post expl
    # pulse_5 = [50, 100, 200]  # expl

    pulse_6 = [200, 205, 250]
    # pulse_6 = [5, 10, 50]
    pulse_0.sort()
    pulse_sr1.sort()
    pulse_c3.sort()
    pulse_5.sort()
    pulse_6.sort()

    if '0' in P.SHS_TO_SHOW:  # BEF EXPL
        _0 = _0_info.Sh_0_info(pulse_0, top_point0)
        infos[_0.id] = _0

    if '1' in P.SHS_TO_SHOW:  # ALL OF THEM. LD NEEDS TO WORK FOR BOTH
        _1 = _1_info.Sh_1_info(pulse_sr1, top_point1)
        infos[_1.id] = _1

    if '2' in P.SHS_TO_SHOW:  # DOWN LEFT
        _2 = _2_info.Sh_2_info(pulse_2, top_point0)
        infos[_2.id] = _2

    if '3' in P.SHS_TO_SHOW and P.A_CS:  # ROCKS
        _3 = _3_info.Sh_3_info(pulse_c3, top_point2)
        infos[_3.id] = _3

    # 4: # DOWN RIGHT

    # 5: 0 but after expl
    if '5' in P.SHS_TO_SHOW:  # POST EXPL
        _5 = _5_info.Sh_5_info(pulse_5, top_point1)
        infos[_5.id] = _5

    if '6' in P.SHS_TO_SHOW:  # EXPL
        _6 = _6_info.Sh_6_info(pulse_6, top_point1)
        infos[_6.id] = _6

    return infos