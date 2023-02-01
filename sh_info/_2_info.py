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

    def __init__(_s, pulse2, top_point):
        super().__init__()
        _s.id = '2'
        _s.extent = "static"
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]

        _s.ld = top_point
        _s.child_names = ['sps', 'ls', 'rs']

        _s.ls_gi = _s.gen_ls_gi(pulse2)

        _s.num_sp_at_init_frame = 50  # OBS this is a special parameter.

        if P.A_SPS:

            '''
            TODO distribute these between them based on pulse2. 
            TODO2: add num sp to generate (50 in main) whenever init frame hit
            '''

            _s.sps_gi0 = _s.gen_sps_gi0()
            _s.sps_gi0['init_frames'] = [10, 50, 70, 100, 250]  # THIS CAUSES IT
            assert(10 + _s.sps_gi0['frames_tot'] + 100 < P.FRAMES_STOP)

            _s.sps_gi2 = _s.gen_sps_gi2()
            _s.sps_gi2['init_frames'] = [30, 100, 150, 200]
            assert(40 + _s.sps_gi2['frames_tot'] + 100 < P.FRAMES_STOP)

            _s.sps_init_frames = _s.sps_gi0['init_frames'] + _s.sps_gi2['init_frames']

        if P.A_RS:
            _s.rs_gi = _s.gen_rs_gi(pulse2)

        _s.zorder = 200

        # _s.sps_gi = copy.deepcopy(_s.sps_gi0)
        # _s.sps_gi['init_frames'] = [10, 40, 222, 300]

    def gen_sps_gi0(_s):

        """
        top left one
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)

        OBS init_frame is set as random.randint(0, 100) in dyn_gen() SHOULD BE MOVED HERE.

        """

        sps_gi = {
            'gi_id': '0',
            'frames_tot': 200,
            'init_frame_max_dist': 100,
            'v_loc': 70, 'v_scale': 16,
            'num_loc': P.NUM_SPS_SH, 'num_scale': P.NUM_SPS_SH / 2,
            'theta_loc': 0.8, 'theta_scale': 0.03,
            'r_f_d_loc': 0.1, 'r_f_d_scale': 0.02,
            'r_f_d_type': 'after',  # which part of r_f_d to use
            'ld': _s.ld,
            'ld_offset_loc': [0, 2],
            'ld_offset_scale': [0, 0.0],
            'R_ss': [0.5, 0.8], 'R_scale': 0.2,
            'G_ss': [0.35, 0.2], 'G_scale': 0.1,
            'B_ss': [0.15, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'up_down': 'down'
        }
        # 160, 77, 36  -> 76, 42, 28


        return sps_gi

    def gen_sps_gi2(_s):

        """
        lower left one
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)
        """

        sps_gi = {
            'gi_id': '2',
            'frames_tot': 230,
            'init_frame_max_dist': 100,  # random num of frames in future from init frame
            'v_loc': 80, 'v_scale': 10,
            'num_loc': P.NUM_SPS_SH, 'num_scale': P.NUM_SPS_SH / 2,
            'theta_loc': 0.8, 'theta_scale': 0.07,
            'r_f_d_loc': 0.1, 'r_f_d_scale': 0.05,
            'r_f_d_type': 'after',  # which part of r_f_d to use
            'ld': _s.ld,
            'ld_offset_loc': [-4, 5],
            'ld_offset_scale': [0, 0],
            # 'R_ss': [0.9, 1], 'R_scale': 0.2,
            # 'G_ss': [0.3, 0.2], 'G_scale': 0.1,
            # 'B_ss': [0.1, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here

            'R_ss': [0.8, 0.9], 'R_scale': 0.2,
            'G_ss': [0.8, 0.2], 'G_scale': 0.1,
            'B_ss': [0.7, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'up_down': 'down'

        }

        # 160, 77, 36  -> 76, 42, 28

        return sps_gi

    def gen_ls_gi(_s, pulse2):

        """

        """

        l_gi = {}
        # l_gi['init_frames'] = [x for x in pulse2]
        l_gi['init_frames'] = [30, 120, 150, 200]
        l_gi['frames_tot'] = 300
        l_gi['ld'] = [_s.ld[0], _s.ld[1] + 10]  # -6 TUNED WITH affine2D.translate!!!
        l_gi['ld_offset_start_loc'] = [-0, 0]  # OBS there is no ss, only start!
        l_gi['ld_offset_start_scale'] = [0, 0]  # OBS there is no ss, only start!
        # l_gi['ld_offset_end_loc'] = [-35, 40]  # OBS there is no ss, only start!
        # l_gi['ld_offset_end_scale'] = [2, 1]  # OBS there is no ss, only start!

        l_gi['ld_offset_end_loc'] = [0, 0]  # OBS there is no ss, only start!
        l_gi['ld_offset_end_scale'] = [0, 0]  # OBS there is no ss, only start!

        l_gi['frame_ss'] = _s.frame_ss  # simpler with this
        l_gi['sr_hardcoded'] = {}
        l_gi['v_loc'] = 30  # rc=2
        l_gi['v_scale'] = 20
        l_gi['theta_loc'] = -0.3  # radians!
        l_gi['theta_scale'] = 0.2
        l_gi['r_f_d_loc'] = 0.05
        l_gi['r_f_d_scale'] = 0.00
        l_gi['zorder'] = 200

        return l_gi

    def gen_rs_gi(_s, init_frames, _type=None):
        rs_gi = {}

        rs_gi['init_frames'] = random.sample(range(1, 300), 50)
        rs_gi['init_frames'].sort()

        # rs_gi['init_frames'] = list(range(3, 63))  # TODO: This should be generated same frame
        rs_gi['frames_tot'] = 200
        # rs_gi['frames_tot'] = 300

        assert (rs_gi['init_frames'][-1] + rs_gi['frames_tot'] < P.FRAMES_STOP)
        rs_gi['ld'] = [_s.ld[0] - 0, _s.ld[1] - 0]  # -6 TUNED WITH affine2D.translate!!!
        rs_gi['ld_offset_loc'] = [-1, 2]  # OBS there is no ss, only start!
        rs_gi['ld_offset_scale'] = [0.2, 0.05]  # OBS there is no ss, only start!
        rs_gi['frame_ss'] = _s.frame_ss  # simpler with this
        rs_gi['rs_hardcoded'] = {}
        rs_gi['v_loc'] = 12  # rc=2
        rs_gi['v_scale'] = 10
        rs_gi['theta_loc'] = np.pi/2 + 0.3  # radians!
        rs_gi['theta_scale'] = 0.02
        rs_gi['r_f_d_loc'] = 0.01
        rs_gi['r_f_d_scale'] = 0.02
        rs_gi['scale_loc'] = 0.15
        rs_gi['scale_scale'] = 0.05
        rs_gi['up_down'] = 'down'
        rs_gi['alpha_plot'] = 'r_down'
        rs_gi['zorder'] = 300

        return rs_gi
