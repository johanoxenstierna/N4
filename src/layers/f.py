from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
import P as P
import numpy as np
from copy import deepcopy

class F(AbstractLayer, AbstractSSS):

    def __init__(_s, id, pic, sh):
        AbstractLayer.__init__(_s)
        _s.id = id
        _s.sh = sh
        _s.pic = pic  # NOT SCALED

        _s.fs_gi = deepcopy(sh.sh_gi.fs_gi)
        _s.zorder = _s.fs_gi['zorder']

        AbstractSSS.__init__(_s, sh, id)
        _s.NUM_FRAMES_F = 150  # 1500 more needed

        _s.sps = {}  # filled with spark instances (not allowed to generate them from inside here).

        # _s.frame_ss = [0, P.FRAMES_STOP - 50]
        # _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]

        '''In N2 below is generated dynamically (probably because there may be some uncertainty regarding
        position of sh, but probably not necessary.'''

        _s.extent, _s.extent_t, lds_vec, _s.scale_vector = gen_extent(_s.fs_gi, pic=_s.pic)
        fun_plot = 'smoka'  # smokr but fun plot is same

        _s.gi = _s.finish_info(_s.fs_gi)

        _s.tri_base, _s.tris, _s.tri_ext, _s.mask_ri, _s.mask_do = \
            gen_triangles(_s.extent_t, _s.extent, _s.gi, _s.pic)


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
