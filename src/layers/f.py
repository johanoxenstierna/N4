

import numpy as np
from copy import deepcopy

import P as P
from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
from src.gen_trig_fun import gen_alpha, gen_scale_lds

class F(AbstractLayer, AbstractSSS):

    def __init__(_s, id, pic, sh):
        AbstractLayer.__init__(_s)
        _s.id = id
        _s.sh = sh
        _s.pic = pic  # NOT SCALED

        _s.gi = deepcopy(sh.sh_gi.fs_gi)
        _s.sps_gi = _s.gen_sps_gi()
        _s.zorder = _s.gi['zorder']

        AbstractSSS.__init__(_s, sh, id)
        # _s.NUM_FRAMES_F = _s.gi['NUM_FRAMES_F']

        _s.sps = {}  # filled with spark instances (not allowed to generate them from inside here).

        # _s.frame_ss = [0, P.FRAMES_STOP - 50]
        # _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]

        '''In N2 below is generated dynamically (probably because there may be some uncertainty regarding
        position of sh, but probably not necessary.'''

        # _s.extent, _s.extent_t, lds_vec, _s.scale_vector = gen_extent(_s.gi, pic=_s.pic)
        fun_plot = 'f'  # smokr but fun plot is same

        _s.gi = _s.finish_info(_s.gi)

        _s.scale_vector = gen_scale_lds(_s.gi['frames_tot'], fun_plot='f')
        _s.rotation = np.linspace(0.01, 1, num=len(_s.scale_vector))
        aa = 5
        # _s.tri_base, _s.tris, _s.tri_ext, _s.mask_ri, _s.mask_do = \
        #     gen_triangles(_s.extent_t, _s.extent, _s.gi, _s.pic)


        _s.alpha = gen_alpha(_s.gi, fun_plot=fun_plot, frames_tot=_s.gi['frames_tot'])

        # _s.temp_x = np.linspace(200, 300, num=_s.gi['frames_tot'])
        # _s.temp_y = np.linspace(50, 50, num=_s.gi['frames_tot'])

        adf = 5

    def gen_scale_vector(_s):

        scale_ss = []
        return scale_ss

    def finish_info(_s, fs_gi):
        """This is written manually and adds/changes things in gi.
        Usually this function is run dynamically depending on coordinates of
        a parent layer at a certain frame. But not always.
        """

        # fs_gi['max_ri'] = np.max(_s.extent[:, 1])

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