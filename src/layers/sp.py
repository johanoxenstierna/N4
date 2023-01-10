"""spark"""

from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
import P as P
import numpy as np
from copy import deepcopy
import random
from src.projective_functions import *

class Sp(AbstractLayer, AbstractSSS):

    def __init__(_s, sh, id_int, f=None):
        AbstractLayer.__init__(_s)

        _s.sh = sh
        _s.id = sh.id + "_f" + "_sp_" + str(id_int)
        if f != None:
            _s.id = sh.id + "_f" + "_sp_" + str(id_int)
            _s.f = f
        #     _s.gi = deepcopy(f.sps_gi)
        #     _s.gi['frames_tot'] = 150
        #     assert(_s.gi['frames_tot'] < _s.f.gi['frames_tot'])
        #     _s._flip_it = True
        #     _s.gi['r_f_d_type'] = 'after'  # after is what is kept
        else:
            _s.f = None
            _s.id = sh.id + "_sp_" + str(id_int)
        #     _s.gi = deepcopy(sh.gi.sps_gi)  # could take it directly from sh but this is simpler
        #     _s.gi['frames_tot'] = sh.gi.sps_gi['frames_tot']
        #     _s._flip_it = True
        #     _s.gi['r_f_d_type'] = 'after'  # after means what is kept

        # _s.frames_tot = f.gi['frames_tot']

        AbstractSSS.__init__(_s, sh, _s.id)
        # # MOVED THIS TO DYN
        # _s.finish_info()
        # _s.zorder = 100
        #
        # '''OBS frames_tot is same as f. But projectile needs to be generated with more frames'''
        # frames_tot_d = int(_s.gi['frames_tot'] * _s.gi['r_f_d'])
        # frames_tot_and_d = _s.gi['frames_tot'] + frames_tot_d
        #
        # _s.xy_t = simple_projectile(v=_s.gi['v'], theta=_s.gi['theta'],
        #                             frames_tot=frames_tot_and_d)
        #
        # _s.xy = shift_projectile(_s.xy_t, origin=(_s.gi['ld'][0] + _s.gi['ld_offset'][0],
        #                                           _s.gi['ld'][1] + _s.gi['ld_offset'][1]),
        #                          frames_tot_d=frames_tot_d,
        #                          flip_it=_flip_it,
        #                          r_f_d_type=_s.gi['r_f_d_type'])
        #
        # _s.alphas = np.linspace(0.6, 0.0, num=len(_s.xy))
        # assert(len(_s.alphas) == len(_s.xy))
        # assert(_s.gi['frames_tot'] == len(_s.alphas))

        adf = 5

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

        R_start = max(0.01, R_start)
        G_start = max(0.01, G_start)
        B_start = max(0.01, B_start)

        _s.R = np.linspace(R_start, _s.gi['R_ss'][1], num=_s.gi['frames_tot'])
        _s.G = np.linspace(G_start, _s.gi['G_ss'][1], num=_s.gi['frames_tot'])
        _s.B = np.linspace(B_start, _s.gi['B_ss'][1], num=_s.gi['frames_tot'])

        try:
            assert(min(_s.R) > 0)
            assert(min(_s.G) > 0)
            assert(min(_s.B) > 0)
        except:
            raise Exception("R G B not within range")

    def dyn_gen(_s, i):

        """
        Basically everything moved from init to here.
        """

        if _s.f != None:
            _s.gi = deepcopy(_s.f.sps_gi)
            _s.gi['frames_tot'] = 150
            assert (_s.gi['frames_tot'] < _s.f.gi['frames_tot'])
            _s._flip_it = True
            _s.gi['r_f_d_type'] = 'after'  # after is what is kept
        else:  # sh sps
            '''Use mod here or smthn'''
            if i == 20:
                _s.gi = deepcopy(_s.sh.gi.sps_gi)  # could take it directly from sh but this is simpler
            elif i == 122:
                _s.gi = deepcopy(_s.sh.gi.sps_gi2)
            elif i == 230:
                _s.gi = deepcopy(_s.sh.gi.sps_gi)

            _s.gi['frames_tot'] = _s.sh.gi.sps_gi['frames_tot']
            _s._flip_it = True
            _s.gi['r_f_d_type'] = 'after'  # after means what is kept

        _s.finish_info()
        _s.zorder = 100

        '''OBS frames_tot is same as f. But projectile needs to be generated with more frames'''
        frames_tot_d = int(_s.gi['frames_tot'] * _s.gi['r_f_d'])
        frames_tot_and_d = _s.gi['frames_tot'] + frames_tot_d

        _s.xy_t = simple_projectile(v=_s.gi['v'], theta=_s.gi['theta'],
                                    frames_tot=frames_tot_and_d)

        _s.xy = shift_projectile(_s.xy_t, origin=(_s.gi['ld'][0] + _s.gi['ld_offset'][0],
                                                  _s.gi['ld'][1] + _s.gi['ld_offset'][1]),
                                 frames_tot_d=frames_tot_d,
                                 flip_it=_s._flip_it,
                                 r_f_d_type=_s.gi['r_f_d_type'])

        _s.alphas = np.linspace(0.6, 0.0, num=len(_s.xy))
        assert (len(_s.alphas) == len(_s.xy))
        assert (_s.gi['frames_tot'] == len(_s.alphas))

