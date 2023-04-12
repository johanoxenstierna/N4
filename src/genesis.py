
import random

import P

# from sh_info import shInfoAbstract, _0_info
from sh_info import _0_info, _1_info, _2_info, _3_info, _4_info, _5_info, _6_info, _7_info, _8_info

def init_infos():
    '''Creates instance of each info and stores in dict'''
    infos = {}

    # top_point0 = [210, 80]
    # top_point1 = [210, 90]  # aft expl
    # top_point2 = [210, 90]  # for 3 rocks

    top_point0 = [545, 330]
    top_point1 = [550, 350]  # aft expl
    top_point_c = [550, 340]  # for 3 rocks
    top_point2 = [550, 330]
    top_point7 = [560, 330]
    EXPL_F = 400

    pulse_sr1 = random.sample(range(5, 800), 70)  # 1 (sr)  # OBS '2' CAN ONLY BE TESTED WHEN STARTS AT 100
    # pulse_sr1 = [110, 150]  # 1 (sr)
    pulse_0 = random.sample(range(50, 500), 25)  # 0 after initial srs
    # pulse_0 = [50, 250]
    pulse_2 = [110, 180, 200, 231, 300, 350]  # THIS IS FOR LS, 1 PER L OBS MAKE SURE THEYRE NOT TOO CLOSE TO EACH OTHER FOR SRS
    # pulse_c3 = random.sample(range(150, 450), 30)  # rs. init_frames use pulse[0] here
    # pulse_3 = [10, 30, 100]  # expl
    pulse_3 = random.sample(range(EXPL_F - 50, EXPL_F + 50), 10)  # post expl FIRST FRAME USED AS REFERENCE FOR C

    pulse_4 = [110, 180, 200, 231, 300, 350]  # THIS IS FOR LS, 1 PER L SEQUENTIAL
    # pulse_4 = [210, 280, 300, 331]  # THIS IS FOR LS, 1 PER L SEQUENTIAL
    pulse_5 = random.sample(range(EXPL_F + 50, EXPL_F + 600), 30)  # post expl
    # pulse_5 = [50, 100, 200]  # expl

    # pulse_6 = [5, 10, 50, 100]
    pulse_6 = [EXPL_F, EXPL_F + 5, EXPL_F + 50]

    # pulse_7 = [10, 40, 80]
    # pulse_7 = [150, 180, 200, 280, 350]
    pulse_7 = [EXPL_F - 50, EXPL_F - 20, EXPL_F, EXPL_F + 20, EXPL_F + 30]

    # TODO AUTOMATE
    pulse_7_sps_dots0 = [EXPL_F - 50, EXPL_F - 20, EXPL_F, EXPL_F + 80, EXPL_F + 150]  # top of mt
    pulse_7_sps_dots1 = [EXPL_F + 101, EXPL_F + 151, EXPL_F + 101, EXPL_F + 351]  # other locs
    pulse_7_sps_dots2 = [EXPL_F + 201, EXPL_F + 251, EXPL_F + 301, EXPL_F + 351]  # other locs
    # pulse_7_sps_dots1 = [10, 20, 30]  # other locs
    pulse_8 = None  # this one is specially set inside 8_info

    pulse_0.sort()
    pulse_sr1.sort()
    pulse_3.sort()
    pulse_5.sort()
    pulse_6.sort()
    pulse_7.sort()

    if '0' in P.SHS_TO_SHOW:  # BEF EXPL
        _0 = _0_info.Sh_0_info(pulse_0, top_point0)
        infos[_0.id] = _0

    if '1' in P.SHS_TO_SHOW:  # ALL OF THEM. LD NEEDS TO WORK FOR BOTH
        _1 = _1_info.Sh_1_info(pulse_sr1, top_point1, EXPL_F)  # OBS shifts pulse_sr1 +30
        infos[_1.id] = _1

    if '2' in P.SHS_TO_SHOW:  # DOWN LEFT
        _2 = _2_info.Sh_2_info(pulse_2, top_point2)
        infos[_2.id] = _2

    if '3' in P.SHS_TO_SHOW and P.A_CS:  # ROCKS
        _3 = _3_info.Sh_3_info(pulse_3, top_point_c)
        infos[_3.id] = _3

    if '4' in P.SHS_TO_SHOW:  # DOWN LEFT
        _4 = _4_info.Sh_4_info(pulse_4, top_point0)
        infos[_4.id] = _4  # DOWN RIGHT

    # 5: 0 but after expl
    if '5' in P.SHS_TO_SHOW:  # POST EXPL
        _5 = _5_info.Sh_5_info(pulse_5, top_point1)
        infos[_5.id] = _5

    if '6' in P.SHS_TO_SHOW:  # EXPL
        _6 = _6_info.Sh_6_info(pulse_6, top_point1)
        infos[_6.id] = _6

    if '7' in P.SHS_TO_SHOW:  # EXTRAS1: srs tied to ls, sps dots
        _7 = _7_info.Sh_7_info(pulse_7, pulse_7_sps_dots0, pulse_7_sps_dots1, pulse_7_sps_dots2, top_point7)
        infos[_7.id] = _7

    if '8' in P.SHS_TO_SHOW:  # EXTRAS2: srs upper
        _8 = _8_info.Sh_8_info(top_point0)
        infos[_8.id] = _8

    return infos