
from sh_info.shInfoAbstract import ShInfoAbstract
import P as P
import random
import numpy as np
import copy

class Sh_1_info(ShInfoAbstract):
    """
    Basically this is the json replacement (also chronicle to some extent).
    Just very basic stuff
    """

    def __init__(_s, pulse, top_point):
        super().__init__()
        _s.id = '1'
        _s.extent = "static"
        _s.child_names = ['srs', 'lis']
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]
        _s.init_frames = pulse
        _s.ld = [top_point[0] - 3, top_point[1] - 5]

        pulse_srs = [x + 30 for x in _s.init_frames]
        _s.srs_gi = {'0': _s.gen_srs_gi(pulse_srs)}  # OBS: sp_gi generated in f class. There is no info class for f.
        _s.srs_gi_init_frames = _s.srs_gi['0']['init_frames']
        _s.zorder = 110

        pulse_lis = [50, 100, 190, 220, 250]
        _s.lis_gi = _s.gen_lis(pulse_lis)

    def gen_srs_gi(_s, pulse_srs):
        """
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        """

        srs_gi = {
            'init_frames': copy.deepcopy(pulse_srs),
            'frames_tot': 300,
            'ld': [_s.ld[0] + 5, _s.ld[1]],
            'ld_offset_loc': [0, 1],
            'ld_offset_scale': [5, 5],
            'scale_ss': [0.01, 3],
            # 'frame_ss': _s.frame_ss,
            'v_loc': 30,  # OBS SPECIAL, USES BEFORE
            'v_scale': 3,
            'theta_loc': -0.9,  # -1.6 is straight up
            'theta_scale': 0.1,
            'rad_rot': 0.2,
            'r_f_d_loc': 0.05,
            'r_f_d_scale': 0.01,
            'up_down': 'up',
            'alpha_range': [0.01, 0.6],
            'zorder': 50,
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_lis(_s, pulse_lis):

        lis_gi = {
            'init_frames': pulse_lis,
            'frames_tot': 7,
            'ld': [_s.ld[0] - 15, _s.ld[1] - 40],
            'ld_offset_loc': [0, 1],
            'ld_offset_scale': [5, 5],
            'zorder': 110,
        }

        return lis_gi





