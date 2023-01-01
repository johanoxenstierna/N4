"""spark"""
from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
import P as P
import numpy as np
from copy import deepcopy
import random
from src.projective_functions import *

class Sp(AbstractLayer, AbstractSSS):

    def __init__(_s, sh, id_int):
        AbstractLayer.__init__(_s)
        _s.id = sh.id + "_sp_" + str(id_int)
        _s.sh = sh

        # _s.fs_gi = f.gi
        _s.gi = deepcopy(sh.gi.sps_gi)  # could take it directly from sh but this is simpler
        _s.finish_info()

        # _s.frames_tot = f.gi['frames_tot']

        AbstractSSS.__init__(_s, sh, _s.id)

        '''OBS frames_tot is same as f. But projectile needs to be generated with more frames'''
        frames_to_discard = int(_s.sh.gi.frames_tot * _s.gi['r_f_d'])
        frames_tot_and_d = _s.sh.gi.frames_tot + frames_to_discard

        _s.xy_t = simple_projectile(v=_s.gi['v'], theta=_s.gi['theta'],
                                    frames_tot=frames_tot_and_d)

        _s.xy = shift_projectile(_s.xy_t, origin=(_s.gi['ld'][0] + _s.gi['ld_offset'][0],
                                                  _s.gi['ld'][1] + _s.gi['ld_offset'][1]),
                                 frames_to_discard=frames_to_discard)

        _s.alphas = np.linspace(0.5, 0.0, num=_s.sh.gi.frames_tot)

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
        _s.gi['ld_offset'] = [np.random.normal(loc=_s.gi['ld_offset_loc'][0], scale=_s.gi['ld_offset_scale'][0]),
                              np.random.normal(loc=_s.gi['ld_offset_loc'][1], scale=_s.gi['ld_offset_scale'][1])]
        _s.zorder = random.randint(_s.sh.gi.zorder - 3, _s.sh.gi.zorder + 0)

        '''Colors'''
        R_start = min(1, np.random.normal(loc=_s.gi['R_ss'][0], scale=_s.gi['R_scale']))
        G_start = min(1, np.random.normal(loc=_s.gi['G_ss'][0], scale=_s.gi['G_scale']))
        B_start = min(1, np.random.normal(loc=_s.gi['B_ss'][0], scale=_s.gi['B_scale']))

        _s.R = np.linspace(R_start, _s.gi['R_ss'][1], num=_s.sh.gi.frames_tot)
        _s.G = np.linspace(G_start, _s.gi['G_ss'][1], num=_s.sh.gi.frames_tot)
        _s.B = np.linspace(B_start, _s.gi['B_ss'][1], num=_s.sh.gi.frames_tot)

