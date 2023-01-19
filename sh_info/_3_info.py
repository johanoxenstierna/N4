import copy

from sh_info.shInfoAbstract import ShInfoAbstract
import P as P
import random
import numpy as np


class Sh_3_info(ShInfoAbstract):
    """
    Basically this is the json replacement (also chronicle to some extent).
    Just very basic stuff
    """

    def __init__(_s):
        super().__init__()
        _s.id = '3'
        _s.extent = "static"
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]  # ONLY ONE WHO USES .
        _s.zorder = 10

        _s.ld = [120, 50]
        _s.child_names = ['cs']  # both cks and cds

        if P.A_CS == 1:  # THEY ALL HAVE INDIVIDUAL GI'S
            _s.cs_gi0 = _s.gen_cs_gi0()  # OBS: sp_gi generated in f class. There is no info class for f.
            # _s.cds_gi = _s.gen_cds_gi(pulse)  # OBS: sp_gi generated in f class. There is no info class for f.

    def gen_cs_gi0(_s, _type=None):
        gi = {}

        '''ck'''
        gi['init_frame'] = 5
        gi['ld'] = [_s.ld[0] - 0, _s.ld[1] - 0]  # -6 TUNED WITH affine2D.translate!!!
        gi['ld_ss'] = [[_s.ld[0], _s.ld[1]], [_s.ld[0] + 50, _s.ld[1]]]  # set extent needs this
        gi['frames_tot'] = 20
        gi['frames_tot1'] = 30
        gi['frame_ss'] = [2, 2 + gi['frames_tot']]  # Konstant
        # gi['frame_ss1'] = [gi['frame_ss'][1], gi['frame_ss'][1] + 30]  # Konstant
        gi['scale_ss'] = [1, 1]
        gi['zorder'] = 5

        '''cd'''



        return gi
