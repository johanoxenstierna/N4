
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

    def __init__(_s, pulse, top_point, EXPL_F):
        super().__init__()
        _s.id = '1'
        _s.extent = "static"
        _s.child_names = ['srs', 'lis', 'fs']
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]
        _s.init_frames = pulse
        _s.ld = [top_point[0] - 3, top_point[1] - 5]

        pulse_srs = [x + 30 for x in _s.init_frames]
        _s.srs_gi = {'0': _s.gen_srs_gi(pulse_srs)}  # OBS: sp_gi generated in f class. There is no info class for f.
        _s.srs_gi_init_frames = _s.srs_gi['0']['init_frames']
        _s.zorder = 200  # in fron t of c

        # pulse_lis = [100, 190, 200, 210, 220, 250, 300]
        pulse_lis = [10, 20, 40, 60, 80, 100, 150, 180, 200, 220, 230, 245, 250, 260, 280, 300]
        pulse_lis = [x + 200 for x in pulse_lis]
        _s.lis_gi = _s.gen_lis_gi(pulse_lis)

        pulse_fs = [EXPL_F]  # shockwave
        _s.fs_gi = _s.gen_fs_gi(pulse_fs)

        pulse_sps = []  # sp hits down

        _s.sps_gi = {}

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
            'v_loc': 26,  # OBS SPECIAL, USES BEFORE
            'v_scale': 3,
            'theta_loc': -0.9,  # -1.6 is straight up
            'theta_scale': 0.1,
            'rad_rot': random.uniform(-0.3, -1.9),
            'r_f_d_loc': 0.05,
            'r_f_d_scale': 0.01,
            'up_down': 'up',
            'alpha_y_range': [0, 0.15],
            'zorder': 50,
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_lis_gi(_s, pulse_lis):

        lis_gi = {
            'init_frames': pulse_lis,
            'frames_tot': None,
            'ld': [_s.ld[0] - 0, _s.ld[1] + 0],
            'ld_offset_loc': [0, 1],
            'ld_offset_scale': [5, 5],
            'zorder': _s.zorder
        }

        return lis_gi

    def gen_fs_gi(_s, pulse):
        """
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        """

        fs_gi = {
            'rad_rot': -0.2,
            'init_frames': pulse,
            'frames_tot': 80,  # MUST BE HIGHTER THAN SP.FRAMES_TOT. BECAUSE WHEN F DELETED,
            'scale_ss': [0.1, 2.0],
            'frame_ss': None,  # simpler with this
            'ld': [_s.ld[0] - 20, _s.ld[1] + 30],
            'x_mov': list(np.linspace(0, -200, num=80)),  # SPECIAL
            'y_mov': list(np.linspace(0, 200, num=80)),  # SPECIAL
            'alpha_y_range': [0, 0.6],
            'zorder': _s.zorder
        }

        return fs_gi





