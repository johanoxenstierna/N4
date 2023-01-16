


import numpy as np
from copy import deepcopy

import P as P
from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
from src.gen_trig_fun import gen_alpha, gen_scale_lds
from src.projective_functions import *

class Sr(AbstractLayer, AbstractSSS):

    def __init__(_s, id, pic, sh):
        AbstractLayer.__init__(_s)
        _s.id = id
        _s.sh = sh
        _s.pic = pic  # NOT SCALED

        _s.gi = deepcopy(sh.gi.srs_gi)
        _s.zorder = _s.gi['zorder']

        AbstractSSS.__init__(_s, sh, id)

        frames_to_d = int(_s.gi['frames_tot'] * _s.gi['r_f_d_loc'])
        frames_tot_and_d = _s.gi['frames_tot'] + frames_to_d

        _s.xy_t = simple_projectile(v=_s.gi['v_loc'], theta=_s.gi['theta_loc'],
                                    frames_tot=frames_tot_and_d, rc=1.3)
        _s.gi = _s.finish_info(_s.gi)

        origin_ = (_s.gi['ld'][0] + _s.gi['ld_offset'][0], _s.gi['ld'][1] + _s.gi['ld_offset'][1])
        _s.xy = shift_projectile(_s.xy_t, origin=origin_, flip_it=True, frames_tot_d=frames_to_d, r_f_d_type='after')

        # _s.extent, _s.extent_t, lds_vec, _s.scale_vector = gen_extent(_s.gi, pic=_s.pic)
        fun_plot = 'sr'  # smokr but fun plot is same

        # _s.scale_vector = gen_scale_lds(_s.gi['frames_tot'], fun_plot='sr')
        _s.scale_vector = np.linspace(0.001, 2.5, num=_s.gi['frames_tot'])
        _s.rotation = np.linspace(0.01, 1, num=len(_s.scale_vector))

        '''CHANGE ALPHA TO NORMAL'''
        _s.alpha = gen_alpha(_s.gi, fun_plot=fun_plot, frames_tot=_s.gi['frames_tot'])

    def gen_scale_vector(_s):

        scale_ss = []
        return scale_ss

    def finish_info(_s, fs_gi):
        """This is written manually and adds/changes things in gi.
        Usually this function is run dynamically depending on coordinates of
        a parent layer at a certain frame. But not always.
        """

        _s.gi['v'] = np.random.normal(loc=_s.gi['v_loc'], scale=_s.gi['v_scale'])
        theta = np.pi / 2 + np.random.normal(loc=_s.gi['theta_loc'], scale=_s.gi['theta_scale'])
        _s.gi['theta'] = theta
        _s.gi['r_f_d'] = np.random.normal(loc=_s.gi['r_f_d_loc'], scale=_s.gi['r_f_d_scale'])
        _s.gi['ld_offset'] = [np.random.normal(loc=_s.gi['ld_offset_loc'][0], scale=_s.gi['ld_offset_scale'][0]),
                              np.random.normal(loc=_s.gi['ld_offset_loc'][1], scale=_s.gi['ld_offset_scale'][1])]

        return fs_gi

    def gen_sps_gi(_s):
        """
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)
        """
        sps_gi = {'v_loc': 12, 'v_scale': 10,
                  'theta_loc': -0.2, 'theta_scale': 0.08,
                  'r_f_d_loc': 0.4, 'r_f_d_scale': 0.05,
                  'origin': (120, 50),
                  'offset_x_loc': 0, 'offset_x_scale': 0.03,
                  'offset_y_loc': 0, 'offset_y_scale': 0.02}
        return sps_gi