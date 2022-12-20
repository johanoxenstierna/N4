"""spark"""
from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
import P as P
import numpy as np
from copy import deepcopy
import random
from src.projective_functions import *

class Sp(AbstractLayer, AbstractSSS):

    def __init__(_s, f, id_int):
        AbstractLayer.__init__(_s)
        _s.id = f.id + "_sp_" + str(id_int)
        _s.f = f

        # _s.fs_gi = f.gi
        _s.gi = deepcopy(f.sps_gi)  # could take it directly from sh but this is simpler
        _s.finish_info()
        _s.zorder = f.gi['zorder']

        # _s.frames_tot = f.gi['frames_tot']

        AbstractSSS.__init__(_s, f.sh, _s.id)

        _s.R = np.linspace(0.9, 1, num=f.gi['frames_tot'])
        _s.G = np.linspace(0.8, 0, num=f.gi['frames_tot'])
        _s.B = np.linspace(0, 0, num=f.gi['frames_tot'])

        '''OBS frames_tot is same as f. But projectile needs to be generated with more frames'''
        frames_to_discard = int(_s.f.gi['frames_tot'] * _s.gi['r_f_d'])
        frames_tot_and_d = _s.f.gi['frames_tot'] + frames_to_discard

        _s.xy_t = simple_projectile(v=_s.gi['v'], theta=_s.gi['theta'],
                                    frames_tot=frames_tot_and_d)

        _s.xy = shift_projectile(_s.xy_t, origin=(_s.gi['origin'][0] + _s.gi['offset_x'], _s.gi['origin'][1] + _s.gi['offset_y']), frames_to_discard=frames_to_discard)

        _s.alphas = np.linspace(0.5, 0.0, num=_s.f.gi['frames_tot'])

        # _s.extent, _s.extent_t, lds_vec, _s.scale_vector = gen_extent(_s.fs_gi, pic=_s.pic)
        # fun_plot = 'smoka'  # smokr but fun plot is same
        #
        # _s.gi = _s.finish_info(_s.fs_gi)
        #
        # _s.tri_base, _s.tris, _s.tri_ext, _s.mask_ri, _s.mask_do = \
        #     gen_triangles(_s.extent_t, _s.extent, _s.gi, _s.pic)


        # _s.alpha = gen_alpha(_s.gi, fun_plot=fun_plot)

    def gen_scale_vector(_s):

        scale_ss = []
        return scale_ss

    def finish_info(_s):
        """This is written manually and adds/changes things in gi.
        Usually this function is run dynamically depending on coordinates of
        a parent layer at a certain frame. But not always.
        """

        # _s.gi['max_ri'] = np.max(_s.extent[:, 1])

        _s.gi['v'] = np.random.normal(loc=_s.gi['v_loc'], scale=_s.gi['v_scale'])
        theta = np.pi / 2 + np.random.normal(loc=_s.gi['theta_loc'], scale=_s.gi['theta_scale'])
        _s.gi['theta'] = theta
        _s.gi['r_f_d'] = np.random.normal(loc=_s.gi['r_f_d_loc'], scale=_s.gi['r_f_d_scale'])
        _s.gi['offset_x'] = np.random.normal(loc=_s.gi['offset_x_loc'], scale=_s.gi['offset_x_scale'])
        _s.gi['offset_y'] = np.random.normal(loc=_s.gi['offset_y_loc'], scale=_s.gi['offset_y_scale'])


