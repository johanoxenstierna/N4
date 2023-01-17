"""the centre of the flame"""

from sh_info.shInfoAbstract import ShInfoAbstract
import P as P
import random
import numpy as np
import copy

class Sh_2_info(ShInfoAbstract):
    """
    Basically this is the json replacement (also chronicle to some extent).
    Just very basic stuff
    """

    def __init__(_s, pulse2):
        super().__init__()
        _s.id = '2'
        _s.extent = "static"
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]
        _s.zorder = 10

        _s.ld = [120, 50]
        _s.child_names = ['sps', 'ls']

        _s.ls_gi = _s.gen_ls_gi(pulse2)
        _s.sps_gi0 = _s.gen_sps_gi0()

        # TODO distribute these between them based on pulse2
        _s.sps_gi0['init_frames'] = [10, 50, 70, 100, 250]  # THIS CAUSES IT
        assert(10 + _s.sps_gi0['frames_tot'] + 100 < P.FRAMES_STOP)

        _s.sps_gi2 = _s.gen_sps_gi2()
        _s.sps_gi2['init_frames'] = [30, 100, 150, 200]
        assert(40 + _s.sps_gi2['frames_tot'] + 100 < P.FRAMES_STOP)

        _s.sps_init_frames = _s.sps_gi0['init_frames'] + _s.sps_gi2['init_frames']

        # _s.sps_gi = copy.deepcopy(_s.sps_gi0)
        # _s.sps_gi['init_frames'] = [10, 40, 222, 300]

    def gen_sps_gi0(_s):

        """
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)
        """

        sps_gi = {
            'gi_id': '0',
            'frames_tot': 200,
            # 'init_frames': [20, 222],  # WHAT HAPPENS IF NEW START EARLY IS THAT OLD ONES DONT GET TIME TO REMOVE THEMSELVES
            # 'init_frames_'
            'v_loc': 70, 'v_scale': 16,
            'num_loc': P.NUM_SPS_SH, 'num_scale': P.NUM_SPS_SH / 2,
            'theta_loc': 0.8, 'theta_scale': 0.03,
            'r_f_d_loc': 0.1, 'r_f_d_scale': 0.02,
            'r_f_d_type': None,  # which part of r_f_d to use
            'ld': _s.ld,
            'ld_offset_loc': [0, 2],
            'ld_offset_scale': [0, 0.0],
            'R_ss': [0.5, 0.8], 'R_scale': 0.2,
            'G_ss': [0.35, 0.2], 'G_scale': 0.1,
            'B_ss': [0.15, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
        }
        # 160, 77, 36  -> 76, 42, 28


        return sps_gi

    def gen_sps_gi2(_s):

        """
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)
        """

        sps_gi = {
            'gi_id': '2',
            'frames_tot': 230,
            # 'init_frames': [20, 222],  # WHAT HAPPENS IF NEW START EARLY IS THAT OLD ONES DONT GET TIME TO REMOVE THEMSELVES
            # 'init_frames_'
            'v_loc': 80, 'v_scale': 10,
            'num_loc': P.NUM_SPS_SH, 'num_scale': P.NUM_SPS_SH / 2,
            'theta_loc': 0.8, 'theta_scale': 0.07,
            'r_f_d_loc': 0.1, 'r_f_d_scale': 0.05,
            'r_f_d_type': None,  # which part of r_f_d to use
            'ld': _s.ld,
            'ld_offset_loc': [-4, 5],
            'ld_offset_scale': [0, 0],
            'R_ss': [0.7, 1], 'R_scale': 0.2,
            'G_ss': [0.3, 0.2], 'G_scale': 0.1,
            'B_ss': [0.1, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
        }
        # 160, 77, 36  -> 76, 42, 28

        return sps_gi

    def gen_ls_gi(_s, pulse2):

        """

        """

        l_gi = {}
        # l_gi['init_frames'] = [x for x in pulse2]
        l_gi['init_frames'] = [10, 50, 100, 150, 200, 250]
        l_gi['frames_tot'] = 200
        l_gi['ld'] = [_s.ld[0], _s.ld[1] + 2]  # -6 TUNED WITH affine2D.translate!!!
        l_gi['ld_offset_start_loc'] = [0, 0]  # OBS there is no ss, only start!
        l_gi['ld_offset_start_scale'] = [0, 0]  # OBS there is no ss, only start!
        l_gi['ld_offset_end_loc'] = [-35, 40]  # OBS there is no ss, only start!
        l_gi['ld_offset_end_scale'] = [2, 1]  # OBS there is no ss, only start!

        l_gi['frame_ss'] = _s.frame_ss  # simpler with this
        l_gi['sr_hardcoded'] = {}
        l_gi['v_loc'] = 30  # rc=2
        l_gi['v_scale'] = 20
        l_gi['theta_loc'] = -0.3  # radians!
        l_gi['theta_scale'] = 0.2
        l_gi['r_f_d_loc'] = 0.05
        l_gi['r_f_d_scale'] = 0.00
        l_gi['zorder'] = 4

        return l_gi




    # def gen_fs_gi(_s):
    #     """
    #     This has to be provided because the fs are generated w.r.t. sh.
    #     This is like the constructor input for F class
    #     """
    #
    #     fs_gi = {}
    #     # fs_gi['init_frames'] = [3, 20, 50, 100, 120, 150, 160, 200]
    #     # init_frames = [20, 40]
    #     init_frames = random.sample(range(1, 300), 20)  # 1-50 is range, 7 is num  + sort
    #     init_frames.sort()
    #     fs_gi['init_frames'] = init_frames
    #     fs_gi['frames_tot'] = random.randint(170, 220)
    #     # fs_gi['ld_offset_ss'] = [[30, -15], [10, -15]]
    #     # fs_gi['ld_offset_rand_ss'] = [[10, 5], [5, 5]]
    #     # fs_gi['scale_ss'] = [0, 12.0]
    #     fs_gi['frame_ss'] = _s.frame_ss  # simpler with this
    #     fs_gi['ld'] = _s.ld
    #     fs_gi['fs_hardcoded'] = {}  # {id: {}}
    #     fs_gi['zorder'] = 5
    #
    #     return fs_gi, init_frames
    #
    # def gen_srs_gi(_s, init_frames):
    #     """
    #     This has to be provided because the fs are generated w.r.t. sh.
    #     This is like the constructor input for F class
    #     """
    #
    #     srs_gi = {}
    #     # srs_gi['init_frames'] = [3, 20, 50, 100, 120, 150, 160, 200]
    #     # init_frames = random.sample(range(1, 200), 10)  # 1-50 is range, 7 is num  + sort
    #     # init_frames.sort()
    #     srs_gi['zorder'] = 4
    #     srs_gi['init_frames'] = init_frames
    #     srs_gi['init_frames'] = [x + 30 for x in srs_gi['init_frames']]
    #
    #     # fs_gi['frames_tot'] = random.randint(170, 220)
    #     srs_gi['frames_tot'] = 300
    #     assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)
    #     srs_gi['ld'] = [_s.ld[0] - 0, _s.ld[1]]  # -6 TUNED WITH affine2D.translate!!!
    #     srs_gi['ld_offset_loc'] = [2, 0]  # OBS there is no ss, only start!
    #     srs_gi['ld_offset_scale'] = [1, 1]  # OBS there is no ss, only start!
    #     # srs_gi['ld_offset_rand'] = [10, 5], [5, 5]
    #     srs_gi['frame_ss'] = _s.frame_ss  # simpler with this
    #     srs_gi['sr_hardcoded'] = {}
    #     srs_gi['v_loc'] = 30  # rc=2
    #     srs_gi['v_scale'] = 20
    #     srs_gi['theta_loc'] = -0.1  # radians!
    #     srs_gi['theta_scale'] = 0.3
    #     srs_gi['r_f_d_loc'] = 0.001
    #     srs_gi['r_f_d_scale'] = 0.00
    #
    #     return srs_gi
    #
    # def gen_rs_gi(_s, init_frames):
    #     rs_gi = {}
    #
    #     rs_gi['zorder'] = 3
    #     # rs_gi['init_frames'] = random.sample(range(1, 60), 60)
    #     rs_gi['init_frames'] = list(range(3, 63))
    #     rs_gi['frames_tot'] = 300
    #
    #     assert (rs_gi['init_frames'][-1] + rs_gi['frames_tot'] < P.FRAMES_STOP)
    #     rs_gi['ld'] = [_s.ld[0] - 0, _s.ld[1] - 0]  # -6 TUNED WITH affine2D.translate!!!
    #     rs_gi['ld_offset_loc'] = [-1, 6]  # OBS there is no ss, only start!
    #     rs_gi['ld_offset_scale'] = [2, 3]  # OBS there is no ss, only start!
    #     rs_gi['frame_ss'] = _s.frame_ss  # simpler with this
    #     rs_gi['rs_hardcoded'] = {}
    #     rs_gi['v_loc'] = 20  # rc=2
    #     rs_gi['v_scale'] = 2
    #     rs_gi['theta_loc'] = -np.pi/2 - 0.3  # radians!
    #     rs_gi['theta_scale'] = 0.2
    #     rs_gi['r_f_d_loc'] = 0.7
    #     rs_gi['r_f_d_scale'] = 0.2
    #
    #     return rs_gi


