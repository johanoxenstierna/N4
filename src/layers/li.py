

import numpy as np
import random
from copy import deepcopy

import P as P
from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
from src.gen_trig_fun import gen_alpha  #, gen_scale_lds

class Li(AbstractLayer, AbstractSSS):

    def __init__(_s, id, pic, sh):
        AbstractLayer.__init__(_s)
        _s.id = id
        _s.sh = sh
        _s.pic = pic  # NOT SCALED

        _s.gi = deepcopy(sh.gi.lis_gi)

        _s.zorder = _s.gi['zorder']

        AbstractSSS.__init__(_s, sh, id)

        # _s.extent = [_s.gi['ld'][0] - 40, _s.gi['ld'][0] + 40,
        #              _s.gi['ld'][1] + 30, _s.gi['ld'][1] - 30]

        '''This is the maximum 12, but not all may be used'''
        _s.alpha = [0.5, 0.7, 0.1, 0.3, 0.2, 0.6, 0.1, 0.3, 0.8, 0.1, 0.9, 0.2, 0.6]

    def finish_info(_s):
        _s.gi['frames_tot'] = random.randint(2, 5)
        # TODO: pick a random sublist from _s.alpha
        _s.gi['rad_rot'] = random.uniform(-1.0, 1.01)
        _s.gi['scale'] = random.uniform(0.2, 0.5)
        _s.gi['ld'][0] += random.uniform(-20, -5)
        _s.gi['ld'][1] += random.uniform(-10, 10)
        # _s.gi['init_frames']
