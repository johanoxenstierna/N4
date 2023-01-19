
"""cliff stationary """

import P as P
# from src.gen_colors import gen_colors
# import copy
import numpy as np
import random

from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
from src.gen_trig_fun import gen_alpha, gen_scale_lds

class C(AbstractLayer, AbstractSSS):
    """Only 1 extent, use alpha to make visible at frames of choice"""
    def __init__(_s, id, pic, sh):
        AbstractLayer.__init__(_s)
        _s.id = id

        '''TODO: Load gi based on pic id'''
        if id[4] == '0':
            _s.gi = sh.gi.cs_gi0
        _s.pic = pic
        _s.l_latest_drawn_id = "99_99_99_99"
        # _s.zorder = _s.gi['zorder']
        AbstractSSS.__init__(_s, sh, id)
        _s.finish_info(id)

        '''OBS THIS GENERATES EXTENT THAT IS TOO LONG'''
        _s.extent_k = np.array([_s.gi['ld'][0], _s.gi['ld'][0] + pic.shape[1],
                                _s.gi['ld'][1], _s.gi['ld'][1] - pic.shape[0]])
        _s.extent, _s.extent_t, lds_vec, _s.scale_vector = gen_extent(_s.gi, pic=_s.pic)
        # _s.extent = _s.extent[0]
        # _s.alpha = gen_alpha(_s.gi, fun_plot='l', frames_tot=_s.gi['frames_tot'], y_range=[0, 0.3])
        _s.alpha = np.full((_s.gi['frames_tot'],), fill_value=1)

        adf = 5

    def finish_info(_s, id):
        pass