


import numpy as np
from copy import deepcopy
import random

import P as P
from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
from src.gen_trig_fun import gen_alpha, gen_scale_lds
from src.projective_functions import *

class R(AbstractLayer, AbstractSSS):

    def __init__(_s, id, pic, sh):
        AbstractLayer.__init__(_s)
        _s.id = id
        _s.sh = sh
        _s.pic = pic  # NOT SCALED

        _s.gi = deepcopy(sh.gi.rs_gi)
        # _s.zorder = _s.gi['zorder']

        AbstractSSS.__init__(_s, sh, id)

        _s.finish_info()
        frames_aft_d = int(_s.gi['frames_tot'] - _s.gi['frames_tot'] * _s.gi['r_f_d'])
        frames_tot_and_d = _s.gi['frames_tot'] + frames_aft_d

        ### HERE: USE pic SHAPE TO CONTROL VELOCITY LOC
        _s.xy_t = simple_projectile(v=_s.gi['v'], theta=_s.gi['theta'],
                                    frames_tot=frames_tot_and_d, rc=1, _type='r')  # OBS upside down!!!!

        # _s.xy_t = np.linspace([10, 50], [80, 10], num=frames_tot_and_d)  #
        _s.R = np.linspace(0.9, 1, num=_s.gi['frames_tot'])
        _s.G = np.linspace(0.8, 0, num=_s.gi['frames_tot'])
        _s.B = np.linspace(0, 0, num=_s.gi['frames_tot'])

        origin_ = (_s.gi['ld'][0] + _s.gi['ld_offset'][0], _s.gi['ld'][1] + _s.gi['ld_offset'][1])
        _s.xy = shift_projectile(_s.xy_t, origin=origin_, flip_it=True, frames_tot_d=frames_aft_d, r_f_d_type='after')
        assert(len(_s.xy) == _s.gi['frames_tot'])
        # _s.extent, _s.extent_t, lds_vec, _s.scale_vector = gen_extent(_s.gi, pic=_s.pic)
        fun_plot = 'r'  # smokr but fun plot is same

        # _s.scale_vector = gen_scale_lds(_s.gi['frames_tot'], fun_plot='sr')
        _s.scale_vector = np.linspace(_s.gi['scale_loc_ss'][0], _s.gi['scale_loc_ss'][1], num=_s.gi['frames_tot'])
        # _s.extent, _s.extent_t = convert_xy_to_extent(_s.xy, _s.scale_vector, _s.gi, _s.pic)
        # _s.gi['max_ri'] = np.max(_s.extent[:, 1])
        # _s.gi['ld_ss'] = [[_s.extent[0, 0], _s.extent[0, 2]], [_s.extent[-1, 0], _s.extent[-1, 2]]]
        # _s.tri_base, _s.tris, _s.tri_ext, _s.mask_ri, _s.mask_do = \
        #     gen_triangles(_s.extent_t, _s.extent, _s.gi, _s.pic)

        # _s.tri_ext['max_do'] = 0
        # _s.tri_ext['max_do'] = 60

        # _s.mask_ri += 50
        # _s.mask_do = 50
        # _s.rotation = np.linspace(0.01, 5, num=len(_s.scale_vector))
        _s.rotation_v = np.linspace(0.01, random.randint(2, 6), num=len(_s.scale_vector))
        # _s.tris, _s.tri_ext = rotate_tris(_s.tris, _s.tri_ext, _s.rotation_v)

        _s.alpha = gen_alpha(_s.gi, fun_plot=fun_plot, frames_tot=_s.gi['frames_tot'])
        '''CHANGE ALPHA TO NORMAL'''

        assert(len(_s.alpha) == _s.gi['frames_tot'])

        fg = 5

    def gen_scale_vector(_s):

        scale_ss = []
        return scale_ss

    def finish_info(_s):
        """This is written manually and adds/changes things in gi.
        Usually this function is run dynamically depending on coordinates of
        a parent layer at a certain frame. But not always.
        """
        _s.gi['zorder'] = random.randint(_s.gi['zorder'] - 1, _s.gi['zorder'] + 1)
        # _s.gi['zorder'] = 4

        # HERE USE PIC
        _s.gi['v'] = np.random.normal(loc=_s.gi['v_loc'], scale=_s.gi['v_scale'])
        theta = np.random.normal(loc=_s.gi['theta_loc'], scale=_s.gi['theta_scale'])
        scale_loc_start = random.uniform(0.1, 0.2)
        scale_loc_stop = scale_loc_start + random.uniform(-0.099, 0.1)
        _s.gi['scale_loc_ss'] = [scale_loc_start, scale_loc_stop]
        _s.gi['theta'] = theta
        _s.gi['r_f_d'] = max(0.01, np.random.normal(loc=_s.gi['r_f_d_loc'], scale=_s.gi['r_f_d_scale']))
        # _s.gi['ld_offset'] = _s.gi['ld_offset_loc']
        _s.gi['ld_offset'] = [np.random.normal(loc=_s.gi['ld_offset_loc'][0], scale=_s.gi['ld_offset_scale'][0]),
                              np.random.normal(loc=_s.gi['ld_offset_loc'][1], scale=_s.gi['ld_offset_scale'][1])]

        '''Since its going both up and down, total y dist must be computed'''
        _s.gi['total_y_dist'] = None


        # _s.gi['v'] = np.random.normal(loc=_s.gi['v_loc'], scale=_s.gi['v_scale'])
        # theta = np.pi / 2 + np.random.normal(loc=_s.gi['theta_loc'], scale=_s.gi['theta_scale'])
        # _s.gi['theta'] = theta
        # _s.gi['r_f_d'] = np.random.normal(loc=_s.gi['r_f_d_loc'], scale=_s.gi['r_f_d_scale'])
        # _s.gi['ld_offset'] = [np.random.normal(loc=_s.gi['ld_offset_loc'][0], scale=_s.gi['ld_offset_scale'][0]),
        #                       np.random.normal(loc=_s.gi['ld_offset_loc'][1], scale=_s.gi['ld_offset_scale'][1])]

    # def gen_sps_gi(_s):
    #     """
    #     THESE ARE AVERAGES
    #     r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
    #     climb up the projectile (before shifting)
    #     """
    #     sps_gi = {'v_loc': 12, 'v_scale': 10,
    #               'theta_loc': -0.2, 'theta_scale': 0.08,
    #               'r_f_d_loc': 0.4, 'r_f_d_scale': 0.05,
    #               'origin': (120, 50),
    #               'offset_x_loc': 0, 'offset_x_scale': 0.03,
    #               'offset_y_loc': 0, 'offset_y_scale': 0.02}
    #     return sps_gi
