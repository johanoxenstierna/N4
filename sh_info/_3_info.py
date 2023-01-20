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

    def __init__(_s, pulse, top_point):
        super().__init__()
        _s.id = '3'
        _s.extent = "static"
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]  # ONLY ONE WHO USES .
        _s.zorder = 10

        _s.ld = [top_point[0] + 8, top_point[1] + 5]
        _s.child_names = ['cs']  # both cks and cds

        if P.A_CS == 1:  # THEY ALL HAVE INDIVIDUAL GI'S
            _s.cs_gi0 = _s.gen_cs_gi0()  # OBS: sp_gi generated in f class. There is no info class for f.
            # _s.cds_gi = _s.gen_cds_gi(pulse)  # OBS: sp_gi generated in f class. There is no info class for f.

    def gen_cs_gi0(_s, _type=None):
        gi = {}

        '''ck'''
        gi['init_frame'] = 5
        # gi['ld'] = [_s.ld[0] - 0, _s.ld[1] - 0]  # -6 TUNED WITH affine2D.translate!!!
        gi['ld'] = [_s.ld[0] - 13, _s.ld[1] + 3]  # -6 TUNED WITH affine2D.translate!!!

        gi['frames_tot'] = 50
        gi['frames_tot1'] = 200

        '''OBS THIS HAS TO BE SECOND BEFORE SET_EXTENT, THEN SET TO FIRST'''
        gi['ld_ss'] = [[gi['ld'][0], gi['ld'][1]], [gi['ld'][0], gi['ld'][1]]]  # set extent needs this
        gi['frame_ss'] = [gi['init_frame'], gi['init_frame'] + gi['frames_tot']]
        gi['frame_ss'] = [gi['frame_ss'][1], gi['frame_ss'][1] + gi['frames_tot1']]
        # gi['frame_ss1'] = [gi['frame_ss'][1], gi['frame_ss'][1] + 30]
        gi['scale_ss'] = [1, 1]


        gi['v'] = 20
        gi['theta'] = -np.pi / 2 + 0.1
        gi['r_f_d'] = 0.01  # THIS MESSES UP START POS
        gi['up_down'] = 'up'

        gi['zorder'] = 90

        '''cd'''



        return gi
