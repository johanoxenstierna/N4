import copy

from sh_info.shInfoAbstract import ShInfoAbstract
import P as P
import random
import numpy as np

class Sh_6_info(ShInfoAbstract):
    """
    Basically this is the json replacement (also chronicle to some extent).
    Just very basic stuff
    """

    def __init__(_s, pulse, top_point):
        super().__init__()
        _s.id = '6'

        _s.extent = "static"
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        # _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]  # ONLY ONE WHO USES .
        _s.zorder = 95

        _s.ld = top_point
        _s.child_names = ['fs', 'srs']
        _s.fs_gi = _s.gen_fs_gi(pulse)  # OBS: sp_gi generated in f class. There is no info class for f.

        if P.A_SRS == 1:
            _s.srs_gi = _s.gen_srs_gi([pulse[0] + 5, pulse[0] + 20, pulse[0] + 35, pulse[0] + 50,
                                       pulse[0] + 75, pulse[0] + 125, pulse[0] + 150,
                                       pulse[0] + 200, pulse[0] + 225, pulse[0] + 250])

            _s.srs_gi_init_frames = [pulse[0] + 5, pulse[0] + 20, pulse[0] + 35, pulse[0] + 50,
                                       pulse[0] + 75, pulse[0] + 125, pulse[0] + 150,
                                       pulse[0] + 200, pulse[0] + 225, pulse[0] + 250]
            _s.srs_gi = {  # these numbers correspond to c!
                '0': _s.srs_gi,
            }
        if P.A_RS == 1:
            pass
            # pulse_rs = random.sample(range(pulse[0], pulse[-1]), 50)
            # pulse_rs.sort()
            # _s.rs_gi = _s.gen_rs_gi(pulse_rs)
        if P.A_SPS == 1:
            _s.sps_gi = _s.gen_sps_gi(pulse)

    def gen_fs_gi(_s, pulse):
        """
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        """
        FRAMES_TOT = 601  # MUST BE HIGHTER THAN SP.FRAMES_TOT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        fs_gi = {
            'rad_rot': -0.2,
            'init_frames': pulse,
            'frames_tot': FRAMES_TOT,
            'scale_ss': [0.01, 1.1],
            'frame_ss': None,  # simpler with this
            'ld': [_s.ld[0] - 2, _s.ld[1]],
            'x_mov': list(np.linspace(0, -15, num=FRAMES_TOT)),  # SPECIAL
            'zorder': 5
        }

        return fs_gi

    def gen_srs_gi(_s, pulse_srs):
        """
        NUKE clouds
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        """

        srs_gi = {
            'init_frames': copy.deepcopy(pulse_srs),
            'frames_tot': 300,
            'ld': [_s.ld[0] - 0, _s.ld[1]],
            'ld_offset_loc': [-4, 15],
            'ld_offset_scale': [1, 1],
            'scale_ss': [0.01, 1.7],
            'frame_ss': _s.frame_ss,
            'v_loc': 50,  # OBS SPECIAL, USES BEFORE
            'v_scale': 0,
            'theta_loc': -0.3,  # -1.6 is straight up
            'theta_scale': 0.02,
            'rad_rot_loc': 0.2,
            'rad_rot_scale': 0.001,
            'r_f_d_loc': 0.1,
            'r_f_d_scale': 0.01,
            'up_down': 'up',
            'alpha_y_range': [0, 0.3],
            'zorder': 20  # nuke
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_sps_gi(_s, init_frames):
        """
        UPDATE: THESE ARE NO LONGER CHILDREN OF F,
        THEIR INIT FRAMES CAN BE SET BY F THOUGH.
        """
        sps_gi = {
            'init_frames': init_frames,  # ONLY FOR THIS TYPE
            'frames_tot': 700,  # MUST BE LOWER THAN SP.FRAMES_TOT. MAYBE NOT. INVOLVED IN BUG
            'v_loc': 50, 'v_scale': 20,
            # 'num_loc': P.NUM_SPS_F, 'num_scale': P.NUM_SPS_F / 2,
            'theta_loc': 1.52, 'theta_scale': 0.2,
            'r_f_d_loc': 0.15, 'r_f_d_scale': 0.13,
            'sp_len_loc': 3, 'sp_len_scale': 100,  # this means that everything will be long, and only slow ones survive
            # 'rad_rot': 0.1,
            'ld': _s.ld,  # in
            'ld_offset_loc': [0, 0],  # NOT USED!!!
            'ld_offset_scale': [5, 5],
            'rgb_start': [0.4, 0.7],  #
            'rgb_theta_diff_c': 0.2,
            'rgb_v_diff_c': 0.001,
            'R_ss': [0.7, 1], 'R_scale': 0.3,  # first one is loc
            'G_ss': [0.4, 0.3], 'G_scale': 0.2,
            'B_ss': [0.3, 0.1], 'B_scale': 0.1,  # good to prevent neg numbers here
            'alpha_y_range': [0.05, 0.4],
            'up_down': 'up'
            # NEED ZORDER
        }

        return sps_gi
