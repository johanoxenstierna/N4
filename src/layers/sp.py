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

        _s.fs_gi = f.fs_gi
        _s.gi = _s.fs_gi
        _s.zorder = f.fs_gi['zorder']

        _s.NUM_FRAMES_F = f.NUM_FRAMES_F

        AbstractSSS.__init__(_s, f.sh, _s.id)

        _s.R = np.linspace(0.9, 1, num=_s.NUM_FRAMES_F)
        _s.G = np.linspace(0.8, 0, num=_s.NUM_FRAMES_F)
        _s.B = np.linspace(0, 0, num=_s.NUM_FRAMES_F)


        # _s.frame_ss = [0, P.FRAMES_STOP - 50]
        # _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]

        '''In N2 below is generated dynamically (probably because there may be some uncertainty regarding
        position of sh, but probably not necessary.'''

        # if random.random() < 0.5:
        # theta = random.randint(299, 300)
        # theta = np.pi

        theta = np.pi/2 + np.random.normal(loc=-.1, scale=0.02)
        # else:
        #     theta = random.randint(357, 360)
        _s.xy_t = simple_projectile(v=np.random.normal(loc=15, scale=5), theta=theta, num_frames=_s.NUM_FRAMES_F)
        _s.xy = shift_projectile(_s.xy_t, (107, 65))

        _s.alphas = np.linspace(0.5, 0.0, num=_s.NUM_FRAMES_F)

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

    def finish_info(_s, fs_gi):
        """This is written manually and adds/changes things in gi.
        Usually this function is run dynamically depending on coordinates of
        a parent layer at a certain frame. But not always.
        """

        fs_gi['max_ri'] = np.max(_s.extent[:, 1])

        return fs_gi