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

    def __init__(_s, pulse):
        super().__init__()
        _s.id = '0'
        _s.extent = "static"
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]  # ONLY ONE WHO USES .
        _s.zorder = 10

        _s.ld = [120, 50]
        _s.child_names = ['fs', 'srs', 'rs']
        _s.fs_gi = _s.gen_fs_gi(pulse)  # OBS: sp_gi generated in f class. There is no info class for f.

        if P.A_SRS == 1:
            _s.srs_gi = _s.gen_srs_gi(pulse)  # OBS: sp_gi generated in f class. There is no info class for f.
        if P.A_RS == 1:
            _s.rs_gi = _s.gen_rs_gi(pulse)  # OBS: sp_gi generated in f class. There is no info class for f.
        if P.A_SPS == 1:
            _s.sps_gi = _s.gen_sps_gi(pulse)  # OBS: sp_gi generated in f class. There is no info class for f.

    def gen_fs_gi(_s, pulse):
        """
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        """

        fs_gi = {}
        # init_frames = [3, 20, 50, 100, 120, 150, 160, 200]
        # init_frames = [10, 20]  # THESE ARE USED FOR SPS NO F AS WELL
        # init_frames = random.sample(range(1, 300), 10)  # 1-50 is range, 7 is num  + sort
        # init_frames.sort()
        fs_gi['init_frames'] = pulse
        # fs_gi['frames_tot'] = random.randint(170, 220)
        fs_gi['frames_tot'] = 151  # MUST BE HIGHTER THAN SP.FRAMES_TOT
        # fs_gi['ld_offset_ss'] = [[30, -15], [10, -15]]
        # fs_gi['ld_offset_rand_ss'] = [[10, 5], [5, 5]]
        # fs_gi['scale_ss'] = [0, 12.0]
        fs_gi['frame_ss'] = _s.frame_ss  # simpler with this
        fs_gi['ld'] = _s.ld
        fs_gi['fs_hardcoded'] = {}  # {id: {}}
        fs_gi['zorder'] = 5

        return fs_gi

    def gen_srs_gi(_s, init_frames):
        """
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        """

        srs_gi = {}
        # srs_gi['init_frames'] = [3, 20, 50, 100, 120, 150, 160, 200]
        # init_frames = random.sample(range(1, 200), 10)  # 1-50 is range, 7 is num  + sort
        # init_frames.sort()
        srs_gi['zorder'] = 4
        srs_gi['init_frames'] = copy.deepcopy(init_frames)


        # srs_gi['init_frames'] = [x + 30 for x in srs_gi['init_frames']]

        # fs_gi['frames_tot'] = random.randint(170, 220)
        srs_gi['frames_tot'] = 300
        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)
        srs_gi['ld'] = [_s.ld[0] - 0, _s.ld[1]]  # -6 TUNED WITH affine2D.translate!!!
        srs_gi['ld_offset_loc'] = [2, 0]  # OBS there is no ss, only start!
        srs_gi['ld_offset_scale'] = [1, 1]  # OBS there is no ss, only start!
        # srs_gi['ld_offset_rand'] = [10, 5], [5, 5]
        srs_gi['frame_ss'] = _s.frame_ss  # simpler with this
        srs_gi['sr_hardcoded'] = {}
        srs_gi['v_loc'] = 30  # rc=2
        srs_gi['v_scale'] = 20
        srs_gi['theta_loc'] = -0.1  # radians!
        srs_gi['theta_scale'] = 0.3
        srs_gi['r_f_d_loc'] = 0.001
        srs_gi['r_f_d_scale'] = 0.00

        return srs_gi

    def gen_rs_gi(_s, init_frames, _type=None):
        rs_gi = {}
        rs_gi['zorder'] = 3
        # rs_gi['init_frames'] = random.sample(range(1, 60), 60)
        rs_gi['init_frames'] = list(range(3, 63))  # TODO: This should be generated same frame
        rs_gi['frames_tot'] = 300
        # rs_gi['frames_tot'] = 300

        assert (rs_gi['init_frames'][-1] + rs_gi['frames_tot'] < P.FRAMES_STOP)
        rs_gi['ld'] = [_s.ld[0] - 0, _s.ld[1] - 0]  # -6 TUNED WITH affine2D.translate!!!
        rs_gi['ld_offset_loc'] = [-1, 2]  # OBS there is no ss, only start!
        rs_gi['ld_offset_scale'] = [0.2, 0.05]  # OBS there is no ss, only start!
        rs_gi['frame_ss'] = _s.frame_ss  # simpler with this
        rs_gi['rs_hardcoded'] = {}
        rs_gi['v_loc'] = 70  # rc=2
        rs_gi['v_scale'] = 22
        rs_gi['theta_loc'] = -np.pi/2 + 0.8  # radians!
        rs_gi['theta_scale'] = 0.02
        rs_gi['r_f_d_loc'] = 0.1
        rs_gi['r_f_d_scale'] = 0.02

        return rs_gi

    def gen_sps_gi(_s, init_frames):
        """
        UPDATE: THESE ARE NO LONGER CHILDREN OF F,
        THEIR INIT FRAMES CAN BE SET BY F THOUGH.
        """
        sps_gi = {
            'init_frames': init_frames,
            # 'frame_ss': [10, 30],
            'frames_tot': None,
            'v_loc': 20, 'v_scale': 5,
            'num_loc': P.NUM_SPS_F, 'num_scale': P.NUM_SPS_F / 2,
            'theta_loc': -0.2, 'theta_scale': 0.3,
            'r_f_d_loc': 0.2, 'r_f_d_scale': 0.05,
            'ld': _s.ld,
            'ld_offset_loc': [0, 1],
            'ld_offset_scale': [0, 0.1],
            'R_ss': [0.9, 1], 'R_scale': 0,
            'G_ss': [0.5, 0.01], 'G_scale': 0.1,
            'B_ss': [0.01, 0.01], 'B_scale': 0,  # good to prevent neg numbers here
        }



        return sps_gi