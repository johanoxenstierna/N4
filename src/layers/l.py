


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
        _s.gi = deepcopy(sh.gi.ls_gi)  # IMPORTANT replaces _s.gi = ship_info
        _s.pic = pic  # NOT SCALED
        _s.l_latest_drawn_id = "99_99_99_99"
        # _s.zorder = _s.gi['zorder']
        AbstractSSS.__init__(_s, sh, id)
        _s.finish_info(id)

        '''OBS THIS GENERATES EXTENT THAT IS TOO LONG'''
        # _s.extent, _s.extent_t, lds_vec, _s.scale_vector = gen_extent(_s.gi, pic=_s.pic)
        # _s.alpha = gen_alpha(_s, frames_tot=_s.gi['frames_tot'], y_range=[0, 0.7])

        adf = 5

    def finish_info(_s, id):
        """
        NO DYN_GEN, so its done here instead
        Ls share gis for a given sh. The sh gi is set with top point, so it is lt,

        The ONLY thing that needs to be done here is extent. id from gen_layers used
        LRDU
        """

        if id[4] == '0':
            extent = [_s.gi['ld'][0] - 6, _s.gi['ld'][0] - 6 + _s.pic.shape[1],
                      _s.gi['ld'][1] + 3, _s.gi['ld'][1] + 3 - _s.pic.shape[0]]
            init_frames = _s.gi['lif0']
            frames_tot = _s.gi['frames_tot0']
            alpha = gen_alpha(_s, frames_tot=frames_tot, y_range=[0, 0.7])
        elif id[4] == '1':
            extent = [_s.gi['ld'][0] - 22, _s.gi['ld'][0] - 22 + _s.pic.shape[1],
                      _s.gi['ld'][1] + 25, _s.gi['ld'][1] + 25 - _s.pic.shape[0]]
            init_frames = _s.gi['lif1']
            frames_tot = _s.gi['frames_tot1']
            alpha = gen_alpha(_s, frames_tot=frames_tot, y_range=[0, 0.7])
        elif id[4] == '2':  # MOVED THIS TO
            extent = [_s.gi['ld'][0] - 60, _s.gi['ld'][0] - 60 + _s.pic.shape[1],
                      _s.gi['ld'][1] + 65, _s.gi['ld'][1] + 65 - _s.pic.shape[0]]
            init_frames = _s.gi['lif2']
        else:
            raise Exception("havent done")

        _s.gi['extent'] = extent
        _s.gi['init_frames'] = init_frames
        _s.alpha = alpha
        _s.gi['frames_tot'] = frames_tot
        # ld_offset_start = [-30, 46]
            # ld_offset_end = [-30, 46]

        # _s.gi['ld'] = [
        #     [_s.gi['ld'][0] + ld_offset_start[0], _s.gi['ld'][1] + ld_offset_start[1]],
        #     [_s.gi['ld'][0] + ld_offset_end[0], _s.gi['ld'][1] + ld_offset_end[1]]
        # ]

