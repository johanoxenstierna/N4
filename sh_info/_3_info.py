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

        _s.ld = [top_point[0] + 0, top_point[1] + 0]
        _s.child_names = ['cs', 'srs']  # both cks and cds

        if P.A_CS == 1:  # THEY ALL HAVE INDIVIDUAL GI'S
            _s.cs_gi0 = _s.gen_cs_gi0()  # OBS: sp_gi generated in f class. There is no info class for f.
            # _s.cds_gi = _s.gen_cds_gi(pulse)  # OBS: sp_gi generated in f class. There is no info class for f.

        if P.A_SRS == 1:
            _s.srs_gi0 = _s.gen_srs_gi0()

        _s.srs_gi = {'init_frames': _s.srs_gi0['init_frames']}

        aa = 5

    def gen_cs_gi0(_s, _type=None):
        gi = {}

        '''ck'''
        gi['init_frame'] = 5
        gi['ld'] = [_s.ld[0] - 0, _s.ld[1] - 0]  # -6 TUNED WITH affine2D.translate!!!
        # gi['ld'] = [_s.ld[0] - 13, _s.ld[1] + 3]  # -6 TUNED WITH affine2D.translate!!!

        gi['frames_tot'] = 30
        gi['frames_tot1'] = 160

        '''OBS THIS HAS TO BE SECOND BEFORE SET_EXTENT, THEN SET TO FIRST'''
        gi['ld_ss'] = [[gi['ld'][0], gi['ld'][1]], [gi['ld'][0], gi['ld'][1]]]  # set extent needs this
        gi['frame_ss'] = [gi['init_frame'], gi['init_frame'] + gi['frames_tot']]
        gi['frame_ss'] = [gi['frame_ss'][1], gi['frame_ss'][1] + gi['frames_tot1']]
        # gi['frame_ss1'] = [gi['frame_ss'][1], gi['frame_ss'][1] + 30]
        gi['scale_ss'] = [1, 1]

        gi['v'] = 30
        gi['theta'] = 0.8 * 2 * np.pi   # 2pi/4 is straight up, 2pi/8 is 45% to right   pos=left, neg=right
        # gi['theta'] = np.pi + 0.001  # 2pi/4 is straight up, 2pi/8 is 45% to right
        gi['r_f_d'] = 0.01  # THIS MESSES UP START POS
        gi['extra_offset_x'] = -1
        gi['up_down'] = 'up'

        gi['zorder'] = 120

        '''cd'''

        return gi

    def gen_srs_gi0(_s):
        """
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        20 sr total init_frames per c.
        """

        srs_gi = {}

        clf = _s.cs_gi0['init_frame'] + _s.cs_gi0['frames_tot'] + _s.cs_gi0['frames_tot1']  # c_last_frame
        frames_tot = 200
        # srs_gi['init_frames'] = [clf - 5, clf - 4, clf - 3, clf, clf + 2]
        # srs_gi['init_frames'] = random.sample(range(50, 200), 20)
        # in_f = random.sample(range(0, frames_tot), 10)  # init_frames starting at frame 0
        # in_f.sort()
        in_f = list(range(clf, clf + 10 * 3, 3))  # AT CRASH, 1 new sr added each frame


        # in_f = [x + clf for x in in_f]

        assert(in_f[-1] < P.FRAMES_STOP)
        srs_gi['init_frames'] = in_f


        # fs_gi['frames_tot'] = random.randint(170, 220)
        srs_gi['frames_tot'] = frames_tot
        assert(srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)
        srs_gi['ld'] = [_s.ld[0] - 0, _s.ld[1]]  # -6 TUNED WITH affine2D.translate!!!
        srs_gi['ld_offset_loc'] = [0, 1]  # OBS there is no ss, only start!
        srs_gi['ld_offset_scale'] = [1, 1]  # OBS there is no ss, only start!
        # srs_gi['ld_offset_rand'] = [10, 5], [5, 5]
        srs_gi['frame_ss'] = _s.frame_ss  # simpler with this
        srs_gi['sr_hardcoded'] = {}
        srs_gi['v_loc'] = 12  # rc=2
        srs_gi['v_scale'] = 2
        srs_gi['theta_loc'] = 0.4 * 2 * np.pi
        srs_gi['theta_scale'] = 0.2
        srs_gi['r_f_d_loc'] = 0.1
        srs_gi['r_f_d_scale'] = 0.00
        srs_gi['up_down'] = 'up'
        srs_gi['zorder'] = 1000

        return srs_gi