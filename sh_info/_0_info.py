import copy

from sh_info.shInfoAbstract import ShInfoAbstract
import P as P
import random
import numpy as np


class Sh_0_info(ShInfoAbstract):
    """
    Basically this is the json replacement (also chronicle to some extent).
    Just very basic stuff
    """

    def __init__(_s, pulse, top_point):
        super().__init__()
        _s.id = '0'

        _s.extent = "static"
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]  # ONLY ONE WHO USES .
        _s.zorder = 110

        _s.ld = top_point
        _s.child_names = ['fs', 'srs', 'rs']

        if P.A_FS:
            _s.fs_gi = _s.gen_fs_gi(pulse)  # OBS: sp_gi generated in f class. There is no info class for f.

        if P.A_SRS == 1:
            srs_init_frames = []
            for init_frame in pulse:
                init_frame_1 = max(30, init_frame)
                if init_frame_1 not in srs_init_frames:
                    srs_init_frames.append(init_frame_1)

            pulse_srs = random.sample(range(pulse[0], pulse[-1]), 50)
            pulse_srs = [max(30, x - 50) for x in pulse_srs]
            _s.srs_gi = _s.gen_srs_gi(pulse_srs)  # OBS: sp_gi generated in f class. There is no info class for f.
            _s.srs_gi_init_frames = _s.srs_gi['init_frames']
            _s.srs_gi = {
                '0': _s.srs_gi,
            }
        if P.A_RS == 1:
            pulse_rs = random.sample(range(pulse[0], pulse[-1]), 50)
            pulse_rs.sort()
            _s.rs_gi = _s.gen_rs_gi(pulse_rs)
        if P.A_SPS == 1:
            _s.sps_gi = _s.gen_sps_gi(pulse)

    def gen_fs_gi(_s, pulse):
        """
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        """

        fs_gi = {
            'rad_rot': -0.2,
            'init_frames': pulse,
            'frames_tot': 151,  # MUST BE HIGHTER THAN SP.FRAMES_TOT. BECAUSE WHEN F DELETED,
            'scale_ss': [0.1, 2.0],
            'frame_ss': None,  # simpler with this
            'ld': [_s.ld[0] - 2, _s.ld[1]],
            'zorder': 5
        }

        return fs_gi

    def gen_srs_gi(_s, pulse_srs):
        """
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        """

        srs_gi = {
            'init_frames': copy.deepcopy(pulse_srs),
            'frames_tot': 250,
            'ld': [_s.ld[0] - 0, _s.ld[1]],
            'ld_offset_loc': [-4, 10],
            'ld_offset_scale': [1, 1],
            'scale_ss': [0.01, 3],
            'frame_ss': _s.frame_ss,
            'v_loc': 25,
            'v_scale': 5,
            'theta_loc': -1.3,  # -1.6 is straight up
            'theta_scale': 0.3,
            'r_f_d_loc': 0.001,
            'r_f_d_scale': 0.1,
            'rad_rot': random.uniform(-0.03, 0.5),
            'up_down': 'up',
            'alpha_y_range': [0.0, 0.3],

            'zorder': None  # Set in finish_info
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_rs_gi(_s, pulse_rs, _type=None):

        rs_gi = {
            'init_frames': pulse_rs,
            'frames_tot': 200,
            'ld': [_s.ld[0] - 0, _s.ld[1] + 3],
            'ld_offset_loc': [0.2, 0.05],
            'ld_offset_scale': [0.2, 0.05],
            'frame_ss': _s.frame_ss,
            'v_loc': 25,
            'v_scale': 5,
            'theta_loc': 1.7,
            'theta_scale': 0.1,
            'r_f_d_loc': 0.7,
            'r_f_d_scale': 0.05,
            'scale_loc': 0.2,
            'scale_scale': 0.08,
            'up_down': 'up',
            'alpha_plot': 'r_up',
            'zorder': 110
        }

        assert (rs_gi['init_frames'][-1] + rs_gi['frames_tot'] < P.FRAMES_STOP)

        return rs_gi

    def gen_sps_gi(_s, init_frames):
        """
        UPDATE: THESE ARE NO LONGER CHILDREN OF F,
        THEIR INIT FRAMES CAN BE SET BY F THOUGH.
        """

        sps_gi = {
            'init_frames': init_frames,  # ONLY FOR THIS TYPE
            'frames_tot': 150,  # MUST BE LOWER THAN SP.FRAMES_TOT. IT CRASHES AT THE LAST FRAME OF THE SP OTHERWISE
            'v_loc': 26, 'v_scale': 8,
            'num_loc': P.NUM_SPS_F, 'num_scale': P.NUM_SPS_F / 2,
            'theta_loc': 1.52, 'theta_scale': 0.05,
            'r_f_d_loc': 0.2, 'r_f_d_scale': 0.05,
            'sp_len_loc': 3, 'sp_len_scale': 8,
            # 'rad_rot': 0.1,
            'ld': _s.ld,  # in
            'ld_offset_loc': [0, 2],
            'ld_offset_scale': [0, 1],
            'rgb_start': [0.4, 0.45],  #
            'rgb_theta_diff_c': 1,
            'rgb_v_diff_c': 0.01,
            'R_ss': [0.9, 1], 'R_scale': 0.5,  # first one is loc
            'G_ss': [0.2, 0.01], 'G_scale': 0.1,
            'B_ss': [0.01, 0.01], 'B_scale': 0,  # good to prevent neg numbers here
            'alpha_y_range': [0.01, 0.7],
            'up_down': 'up'
        }

        return sps_gi