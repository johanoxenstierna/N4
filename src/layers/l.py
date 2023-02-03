


import P as P
# from src.gen_colors import gen_colors
# import copy
import numpy as np
import random

from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
from src.gen_trig_fun import gen_alpha, gen_scale_lds

class L(AbstractLayer, AbstractSSS):
    """Only 1 extent, use alpha to make visible at frames of choice"""
    def __init__(_s, id, pic, sh):
        AbstractLayer.__init__(_s)
        _s.id = id
        _s.gi = sh.gi.ls_gi  # IMPORTANT replaces _s.gi = ship_info
        _s.pic = pic  # NOT SCALED
        _s.l_latest_drawn_id = "99_99_99_99"
        # _s.zorder = _s.gi['zorder']
        AbstractSSS.__init__(_s, sh, id)
        _s.finish_info(id)

        '''OBS THIS GENERATES EXTENT THAT IS TOO LONG'''
        _s.extent, _s.extent_t, lds_vec, _s.scale_vector = gen_extent(_s.gi, pic=_s.pic)
        _s.extent = _s.extent[0]
        _s.alpha = gen_alpha(_s, frames_tot=_s.gi['frames_tot'], y_range=[0, 0.3])

        adf = 5

    def finish_info(_s, id):

        _s.gi['scale_ss'] = [0.4, 0.4]

        if id[4] == '0':
            ld_offset_start = [-4, 6]
            ld_offset_end = [-4, 6]
        elif id[4] == '1':
            ld_offset_start = [-10, 13]
            ld_offset_end = [-10, 13]
        elif id[4] == '2':
            ld_offset_start = [-30, 29]
            ld_offset_end = [-30, 29]
        else:
            a = 5
            # ld_offset_start = [-30, 46]
            # ld_offset_end = [-30, 46]

        _s.gi['ld_ss'] = [
            [_s.gi['ld'][0] + ld_offset_start[0], _s.gi['ld'][1] + ld_offset_start[1]],
            [_s.gi['ld'][0] + ld_offset_end[0], _s.gi['ld'][1] + ld_offset_end[1]]
        ]

