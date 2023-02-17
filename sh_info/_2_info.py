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

    def __init__(_s, pulse, top_point):
        super().__init__()
        _s.id = '2'
        _s.extent = "static"
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]  # l frames_tot set below

        _s.ld = top_point
        _s.child_names = ['sps', 'ls', 'rs']

        '''DOESNT CARE ABOUT LS for now. OBS WATCH OVERLAP'''
        l_init_frames0 = [90, 110]
        # l_init_frames0 = [x + 100 for x in l_init_frames0]
        l_init_frames1 = [120, 180]
        # l_init_frames1 = [x + 100 for x in l_init_frames1]180
        # l_init_frames = [130, 220, 250, 300]
        l_init_frames = [90, 120, 110, 180]
        # l_init_frames = [x + 100 for x in l_init_frames]
        # l_init_frames = [10, 30, 60, 300]
        _s.ls_gi = _s.gen_ls_gi(l_init_frames)

        # _s.num_sp_at_init_frame = 50  # OBS this is a special parameter.  # P instead

        if P.A_SPS:

            '''
            TODO distribute these between them based on pulse. 
            TODO2: add num sp to generate (50 in main) whenever init frame hit
            L needs to be generated based on these. 
            '''

            init_frames = []
            _s.sps_gi0, init_frames = _s.gen_sps_gi0(init_frames, l_init_frames0)
            # _s.sps_gi0['init_frames'] = [110, 150, 170, 200, 350]  # THIS CAUSES IT
            # assert(10 + _s.sps_gi0['frames_tot'] + 100 < P.FRAMES_STOP)

            _s.sps_gi2, init_frames = _s.gen_sps_gi2(init_frames, l_init_frames1)
            # _s.sps_gi2['init_frames'] = [130, 200, 250, 300]
            # assert(40 + _s.sps_gi2['frames_tot'] + 100 < P.FRAMES_STOP)

            _s.sps_gi = {
                '0': _s.sps_gi0,
                '2': _s.sps_gi2
            }
            init_frames.sort()
            _s.sps_gi_init_frames = init_frames

        if P.A_RS:
            rs_init_frames = random.sample(range(pulse[0], pulse[-1]), 50)
            _s.rs_gi = _s.gen_rs_gi(rs_init_frames)

        _s.zorder = 130

        # _s.sps_gi = copy.deepcopy(_s.sps_gi0)
        # _s.sps_gi['init_frames'] = [10, 40, 222, 300]

    def gen_ls_gi(_s, l_init_frames):

        """
        SHARED FOR THE SAME SH. Kind of... makes sense. ld is used for extent, but they are modified
        for each l in l class finish info.
        """

        l_gi = {
            'init_frames': l_init_frames,
            'frames_tot': 150,
            'ld': [_s.ld[0] - 5, _s.ld[1] + 20],  # top point!!! morphd to extent in l finish_info
            'frame_ss': _s.frame_ss,
            'zorder': 120  # 3 is 110
        }

        return l_gi

    def gen_sps_gi0(_s, init_frames, l_init_frames):

        """
        MATCHED WITH ls gi, BUT THEYRE NOT CHILDREN AS FOR F -> SP (bcs problem there is that when F dies, then
        so does sp, so f has to last longer than sp).
        top left one
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)

        OBS init_frame is set as random.randint(0, 100) in dyn_gen() SHOULD BE MOVED HERE.

        """

        init_frames_sp = []
        for i in range(len(l_init_frames)):
            init_frame_sp = max(10, l_init_frames[i] - 70)  # OBS first number needs to be different for each sp
            if init_frame_sp in init_frames:
                raise Exception("cs sp init_frame already exists. Change frames_tot1 of c0")
            else:
                init_frames_sp.append(init_frame_sp)
                init_frames.append(init_frame_sp)

        sps_gi = {
            'gi_id': '0',
            'init_frames': init_frames_sp,
            'frames_tot': 100,
            'init_frame_max_dist': 40,  # OBS THIS MUST BE SHORTER
            'v_loc': 80, 'v_scale': 12,
            # 'num_loc': P.NUM_SPS_L, 'num_scale': P.NUM_SPS_L / 2,
            'theta_loc': -1.1, 'theta_scale': 0.05,  # neg is left  with straight down= -1.6, 0=
            'r_f_d_loc': 0.1, 'r_f_d_scale': 0.02,
            'r_f_d_type': 'after',  # which part of r_f_d to use
            'sp_len_loc': 5, 'sp_len_scale': 5,
            'ld': [_s.ld[0] + 3, _s.ld[1] - 5],
            'ld_offset_loc': [0, 2],
            'ld_offset_scale': [0, 1],
            'R_ss': [0.9, 1], 'R_scale': 0.2,
            'G_ss': [0.5, 0.2], 'G_scale': 0.15,
            'B_ss': [0.2, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'up_down': 'down'
        }

        return sps_gi, init_frames

    def gen_sps_gi2(_s, init_frames, l_init_frames):

        """
        lower left one
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)
        """

        init_frames_sp = []
        for i in range(len(l_init_frames)):
            init_frame_sp = max(10, l_init_frames[i] - 70)  # OBS first number needs to be different for each sp
            if init_frame_sp in init_frames:
                raise Exception("cs sp init_frame already exists. Change frames_tot1 of c0")
            else:
                init_frames_sp.append(init_frame_sp)
                init_frames.append(init_frame_sp)

        sps_gi = {
            'gi_id': '2',
            'init_frames': init_frames_sp,
            'frames_tot': 100,
            'init_frame_max_dist': 35,  # random num of frames in future from init frame
            'v_loc': 90, 'v_scale': 6,
            # 'num_loc': P.NUM_SPS_F, 'num_scale': P.NUM_SPS_F / 2,
            'theta_loc': -0.9, 'theta_scale': 0.03,
            'r_f_d_loc': 0.1, 'r_f_d_scale': 0.05,
            'r_f_d_type': 'after',  # which part of r_f_d to use
            'sp_len_loc': 5, 'sp_len_scale': 5,
            'ld': [_s.ld[0] - 0, _s.ld[1] + 10],
            'ld_offset_loc': [-4, 5],
            'ld_offset_scale': [0, 1],
            'R_ss': [0.8, 1], 'R_scale': 0.2,
            'G_ss': [0.4, 0.2], 'G_scale': 0.2,
            'B_ss': [0.1, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'up_down': 'down'
        }

        # 160, 77, 36  -> 76, 42, 28

        return sps_gi, init_frames



    def gen_rs_gi(_s, rs_init_frames, _type=None):
        rs_gi = {}

        rs_gi['init_frames'] = rs_init_frames
        rs_gi['init_frames'].sort()

        # rs_gi['init_frames'] = list(range(3, 63))  # TODO: This should be generated same frame
        rs_gi['frames_tot'] = 200
        # rs_gi['frames_tot'] = 300

        assert (rs_gi['init_frames'][-1] + rs_gi['frames_tot'] < P.FRAMES_STOP)
        rs_gi['ld'] = [_s.ld[0] - 0, _s.ld[1] - 0]  # -6 TUNED WITH affine2D.translate!!!
        rs_gi['ld_offset_loc'] = [-1, 2]  # OBS there is no ss, only start!
        rs_gi['ld_offset_scale'] = [0.2, 1]  # OBS there is no ss, only start!
        rs_gi['frame_ss'] = _s.frame_ss  # simpler with this
        rs_gi['rs_hardcoded'] = {}
        rs_gi['v_loc'] = 100  # rc=2
        rs_gi['v_scale'] = 20
        rs_gi['theta_loc'] = -1.0  # radians!
        rs_gi['theta_scale'] = 0.1
        rs_gi['r_f_d_loc'] = 0.1
        rs_gi['r_f_d_scale'] = 0.02
        rs_gi['scale_loc'] = 0.17
        rs_gi['scale_scale'] = 0.05
        rs_gi['up_down'] = 'down'
        # rs_gi['alpha_plot'] = 'r_down'
        rs_gi['zorder'] = 300

        return rs_gi
