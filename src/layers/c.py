
"""cliff stationary """

import P as P
# from src.gen_colors import gen_colors
# import copy
import numpy as np
import random

from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
from src.gen_trig_fun import gen_alpha, gen_scale_lds
from src.projective_functions import *

class C(AbstractLayer, AbstractSSS):
    """Only 1 extent, use alpha to make visible at frames of choice"""
    def __init__(_s, id, pic, sh):
        AbstractLayer.__init__(_s)
        _s.id = id

        _s.gi = _s.load_gi(id, sh)

        _s.pic = pic
        _s.l_latest_drawn_id = "99_99_99_99"
        # _s.zorder = _s.gi['zorder']
        AbstractSSS.__init__(_s, sh, id)
        # _s.finish_info(id)

        '''OBS THIS GENERATES EXTENT THAT IS TOO LONG'''
        _s.extent_k = np.array([_s.gi['ld'][0], _s.gi['ld'][0] + pic.shape[1],
                                _s.gi['ld'][1], _s.gi['ld'][1] - pic.shape[0]])
        # _s.extent, _s.extent_t, lds_vec, _s.scale_vector = gen_extent(_s.gi, pic=_s.pic)
        # _s.extent_k = _s.extent[0]
        # assert(len(_s.extent) == _s.gi['frames_tot1'])

        frames_aft_d = int(_s.gi['frames_tot1'] - _s.gi['frames_tot1'] * _s.gi['r_f_d'])
        frames_tot_and_d = _s.gi['frames_tot1'] + frames_aft_d

        _s.xy_t = simple_projectile(v=_s.gi['v'], theta=_s.gi['theta'],
                                    frames_tot=frames_tot_and_d, rc=1, up_down=_s.gi['up_down'])  # OBS upside down!!!!
        origin_ = (_s.gi['ld'][0], _s.gi['ld'][1])

        _s.xy = shift_projectile(_s.xy_t, origin=origin_, up_down=_s.gi['up_down'], frames_tot_d=frames_aft_d,
                                 r_f_d_type='after')

        _s.scale_vector = np.linspace(1, 1, num=_s.gi['frames_tot1'])
        _s.extent, _s.extent_t = convert_xy_to_extent(_s.xy, _s.scale_vector, _s.gi, _s.pic)

        _s.gi['max_ri'] = np.max(_s.extent[:, 1])
        _s.tri_base, _s.tris, _s.tri_ext, _s.mask_ri, _s.mask_do = \
                gen_triangles(_s.extent_t, _s.extent, _s.gi, _s.pic)

        _s.mask_ri += _s.gi['extra_offset_x']
        _s.mask_do += _s.gi['extra_offset_y']

        # '''HINT: V AFFECTS THIS'''
        # if _s.extent[0, 2] < _s.extent[-1, 2]:  # this means r_f_d was used (object fell). SHOULD ALWAYS BE TRUE
        #     r_f_d_span_y = _s.extent[-1, 2] - _s.extent[0, 2]
        #     _s.mask_do += int(r_f_d_span_y) - 0

        # _s.mask_ri += 0  # TODO: BUG HERE NOT SURE HOW TO FIX.

        # _s.extent = _s.extent[0]
        _s.alpha = gen_alpha(_s, frames_tot=_s.gi['frames_tot1'], y_range=[0, 1])
        # _s.alpha = np.full((_s.gi['frames_tot1'],), fill_value=1)  # OBS only set for frames_tot1
        # _s.alpha = np.linspace(1, 1, num=len(_s.extent))

        # rad_rot = None
        # if _s.gi['theta'] < 0:
        #     rad_rot = 1
        # else:
        #     rad_rot = -1
        _s.rotation_v = np.linspace(0.00, _s.gi['rad_rot'], num=len(_s.alpha))
        _s.tris, _s.tri_ext = rotate_tris(_s.tris, _s.tri_ext, _s.rotation_v)

        _s.check_extents()
        asdf = 5

    def load_gi(_s, id, sh):
        '''TODO: Load gi based on pic id'''
        id_s = id.split('_')[2]

        if id_s == '0':
            gi = sh.gi.cs_gi0
        elif id_s == '1':
            gi = sh.gi.cs_gi1
        elif id_s == '2':
            gi = sh.gi.cs_gi2
        elif id_s == '3':
            gi = sh.gi.cs_gi3
        elif id_s == '4':
            gi = sh.gi.cs_gi4
        elif id_s == '5':
            gi = sh.gi.cs_gi5
        elif id_s == '6':
            gi = sh.gi.cs_gi6
        elif id_s == '7':
            gi = sh.gi.cs_gi7
        elif id_s == '8':
            gi = sh.gi.cs_gi8
        elif id_s == '9':
            gi = sh.gi.cs_gi9
        elif id_s == '10':
            gi = sh.gi.cs_gi10
        else:
            raise Exception("Probably have to sort out images/processed/" + id_s)

        return gi
