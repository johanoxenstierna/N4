

import numpy as np
from copy import deepcopy

import P as P
from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
from src.gen_trig_fun import gen_alpha, gen_scale_lds

class Li(AbstractLayer, AbstractSSS):

    def __init__(_s, id, pic, sh):
        AbstractLayer.__init__(_s)
        _s.id = id
        _s.sh = sh
        _s.pic = pic  # NOT SCALED

        _s.gi = deepcopy(sh.gi.lis_gi)

        _s.zorder = _s.gi['zorder']

        AbstractSSS.__init__(_s, sh, id)

        _s.extent = [_s.gi['ld'][0] - 40, _s.gi['ld'][0] + 40,
                     _s.gi['ld'][1] + 30, _s.gi['ld'][1] - 30]

        _s.alpha = [0.5, 0.7, 0.1, 0.3, 0.2, 0.6, 0.1]

        # _s.extent, _s.extent_t, lds_vec, _s.scale_vector = gen_extent(_s.gi, pic=_s.pic)