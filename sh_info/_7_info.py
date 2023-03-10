
from sh_info.shInfoAbstract import ShInfoAbstract
import P as P
import random
import numpy as np
import copy

class Sh_7_info(ShInfoAbstract):
    """
    Extras. For now try to do just 1 at init_frame with low alpha.
    Basically this is the json replacement (also chronicle to some extent).
    Just very basic stuff
    """

    def __init__(_s, pulse, top_point):
        super().__init__()
        _s.id = '7'
        _s.extent = "static"
        _s.child_names = ['ls', 'srs', 'sps']
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.init_frames = pulse
        _s.ld = top_point

        _s.ls_gi = _s.gen_ls_gi(pulse)  # NO DYN_GEN
        pulse_srs = _s.gen_pulse_srs7(pulse)
        _s.srs_gi = {'0': _s.gen_srs_gi(pulse_srs)}
        _s.srs_gi_init_frames = _s.srs_gi['0']['init_frames']

        init_frames_sp0 = [20]
        # init_frames_sp1 = [40]  # 150 is init_frame_max_dist
        # init_frames_sp2 = [60]  # 150 is init_frame_max_dist
        # init_frames_sp3 = [pulse[3] - 100, pulse[3], pulse[3] + 100]  # 150 is init_frame_max_dist

        _s.sps_gi0 = _s.gen_sps_gi0(init_frames_sp0)
        # _s.sps_gi1 = _s.gen_sps_gi1(init_frames_sp1)
        # _s.sps_gi2 = _s.gen_sps_gi2(init_frames_sp2)
        # _s.sps_gi3 = _s.gen_sps_gi3(init_frames_sp3)
        _s.sps_gi_init_frames = init_frames_sp0 #+ init_frames_sp1 + init_frames_sp2

        _s.sps_gi = {
            '0': _s.sps_gi0
            # '1': _s.sps_gi1,
            # '2': _s.sps_gi2
            # '3': _s.sps_gi3
        }

        _s.zorder = 300

    def gen_ls_gi(_s, pulse):
        """
        SHARED FOR THE SAME SH. Kind of... makes sense. ld is used for extent, but they are modified
        for each l in l class finish info.
        """

        # lif0, lif1 = _s.distribute_pulse_for_ls(pulse)  # l_init_frame
        lif0 = [pulse[0]]
        lif1 = [pulse[1]]  # OBS REMEMBER l_init_frames below
        lif2 = [pulse[2]]  # OBS REMEMBER l_init_frames below
        # lif2 = [pulse[2]]
        # lif3 = [pulse[3]]
        l_init_frames = lif0 + lif1 + lif2 #+ lif3

        ls_gi = {
            'init_frames_all': l_init_frames,
            'lif0': lif0,
            'lif1': lif1,
            'lif2': lif2,
            # 'lif2': lif2,
            # 'lif3': lif3,
            'frames_tot0': 100,
            'frames_tot1': 100,
            'frames_tot2': 100,
            # 'frames_tot2': 500,
            # 'frames_tot3': 500,
            'ld': _s.ld,
            'ld0': [_s.ld[0] + 22, _s.ld[1] + 158],
            'ld1': [_s.ld[0] + 89, _s.ld[1] + 152],
            'ld2': [_s.ld[0] - 74, _s.ld[1] + 122],
            'frame_ss': _s.frame_ss,
            'zorder': 120  # 3 is 110
        }

        return ls_gi

    def gen_pulse_srs7(_s, pulse):

        pulse_srs = []
        for init_frame in pulse:
            for i in range(-10, 10, 3):  # 5 total for each ls
                init_frame_sr_cand = init_frame + i
                if init_frame_sr_cand not in pulse_srs:
                    pulse_srs.append(init_frame_sr_cand)

        return pulse_srs

    def gen_srs_gi(_s, pulse_srs):
        """
        Tied to ls!
        """

        srs_gi = {
            'init_frames': copy.deepcopy(pulse_srs),
            'frames_tot': 300,
            'ld': None,  # finish_info
            'ld_offset_loc': [0, 0],
            'ld_offset_scale': [0, 0],
            'scale_ss': [0.01, 0.5],  # assumed big pics
            # 'frame_ss': _s.frame_ss,
            'v_loc': 25,  # OBS SPECIAL, USES BEFORE
            'v_scale': 5,
            'theta_loc': -0.3,  # -1.6 is straight up
            'theta_scale': 0.1,
            'rad_rot': random.uniform(-0.1, -0.3),
            'r_f_d_loc': 0.05,
            'r_f_d_scale': 0.01,
            'up_down': 'up',
            'alpha_y_range': [0, 0.6],
            'zorder': 200,
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_sps_gi0(_s, init_frames_sp):

        """
        MATCHED WITH ls gi, BUT THEYRE NOT CHILDREN AS FOR F -> SP (bcs problem there is that when F dies, then
        so does sp, so f has to last longer than sp).
        top left one
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)

        OBS init_frame is set as random.randint(0, 100) in dyn_gen() SHOULD BE MOVED HERE.

        """

        sps_gi = {
            'gi_id': '0',
            'init_frames': init_frames_sp,
            'frames_tot': 120,  # NEEDS TO MATCH WITH EXPL
            'init_frame_max_dist': 100,  # OBS THIS MUST BE SHORTER
            'v_loc': 50, 'v_scale': 15,
            # 'num_loc': P.NUM_SPS_L, 'num_scale': P.NUM_SPS_L / 2,
            'theta_loc': -1.6, 'theta_scale': 1,  # neg is left  with straight down= -1.6, 0=
            'r_f_d_loc': 0.1, 'r_f_d_scale': 0.3,
            'r_f_d_type': 'after',  # which part of r_f_d to use
            'sp_len_loc': 2, 'sp_len_scale': 4,
            'rgb_start': [0.4, 0.9],  #
            'rgb_theta_diff_c': 0.0,
            'rgb_v_diff_c': 0.01,
            'ld': _s.ld,
            'ld_offset_loc': [1, 20],
            'ld_offset_scale': [5, 5],
            # 'R_ss': [0.9, 1], 'R_scale': 0.2,
            # 'G_ss': [0.5, 0.2], 'G_scale': 0.15,
            # 'B_ss': [0.2, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'alpha_y_range': [0.01, 0.4],
            'up_down': 'down'
        }

        return sps_gi

    def gen_sps_gi1(_s, init_frames_sp):

        """
        lower left one
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)
        """

        # init_frames_sp = []

        # BELOW IS TOO BRITTLE.
        # init_frames_to_rem = []  # these are removed afterwards
        # for i in range(len(_s.ls_gi['lif1'])):
        #     init_frame_sp = max(10, _s.ls_gi['lif1'][i] - 150)  # OBS first number needs to be different for each sp
        #     if init_frame_sp in init_frames:
        #         init_frames_to_rem.append(init_frame_sp)
        #         # raise Exception("cs sp init_frame already exists. Change frames_tot1 of c0")
        #     else:
        #         init_frames_sp.append(init_frame_sp)
        #         init_frames.append(init_frame_sp)
        #
        # '''remove duplicates'''
        # init_frames = [x for x in init_frames if x not in init_frames_to_rem]
        # _s.ls_gi['lif1'] = [x for x in _s.ls_gi['lif1'] if x not in init_frames_to_rem]


        sps_gi = {
            'gi_id': '1',
            'init_frames': init_frames_sp,
            'frames_tot': 150,
            'init_frame_max_dist': 100,  # random num of frames in future from init frame
            'v_loc': 100, 'v_scale': 10,
            # 'num_loc': P.NUM_SPS_F, 'num_scale': P.NUM_SPS_F / 2,
            'theta_loc': -0.9, 'theta_scale': 0.03,
            'r_f_d_loc': 0.1, 'r_f_d_scale': 0.05,
            'r_f_d_type': 'after',  # which part of r_f_d to use
            'rgb_start': [0.4, 0.45],  #
            'rgb_theta_diff_c': 1,
            'rgb_v_diff_c': 0.01,
            'sp_len_loc': 5, 'sp_len_scale': 15,
            'ld': [_s.ld[0] - 0, _s.ld[1] + 10],
            'ld_offset_loc': [-4, 5],
            'ld_offset_scale': [0, 1],
            'R_ss': [0.8, 1], 'R_scale': 0.2,
            'G_ss': [0.4, 0.2], 'G_scale': 0.2,
            'B_ss': [0.1, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'alpha_y_range': [0.05, 0.9],
            'up_down': 'down'
        }

        # 160, 77, 36  -> 76, 42, 28

        return sps_gi

    def gen_sps_gi2(_s, init_frames_sp):

        """
        lower left one
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)
        """

        sps_gi = {
            'gi_id': '2',
            'init_frames': init_frames_sp,
            'frames_tot': 150,
            'init_frame_max_dist': 100,  # random num of frames in future from init frame
            'v_loc': 100, 'v_scale': 10,
            'theta_loc': -0.7, 'theta_scale': 0.03,
            'r_f_d_loc': 0.1, 'r_f_d_scale': 0.05,
            'r_f_d_type': 'after',  # which part of r_f_d to use
            'rgb_start': [0.4, 0.45],  #
            'rgb_theta_diff_c': 1,
            'rgb_v_diff_c': 0.01,
            'sp_len_loc': 5, 'sp_len_scale': 15,
            'ld': [_s.ld[0] - 0, _s.ld[1] + 10],
            'ld_offset_loc': [-25, 35],
            'ld_offset_scale': [0, 1],
            'R_ss': [0.8, 1], 'R_scale': 0.2,
            'G_ss': [0.4, 0.2], 'G_scale': 0.2,
            'B_ss': [0.1, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'alpha_y_range': [0.05, 0.9],
            'up_down': 'down'
        }

        # 160, 77, 36  -> 76, 42, 28

        return sps_gi

    def gen_sps_gi3(_s, init_frames_sp):

        """
        lower left one
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)
        """

        sps_gi = {
            'gi_id': '3',
            'init_frames': init_frames_sp,
            'frames_tot': 150,
            'init_frame_max_dist': 100,  # random num of frames in future from init frame
            'v_loc': 100, 'v_scale': 10,
            # 'num_loc': P.NUM_SPS_F, 'num_scale': P.NUM_SPS_F / 2,
            'theta_loc': -1.1, 'theta_scale': 0.1,
            'r_f_d_loc': 0.1, 'r_f_d_scale': 0.05,
            'r_f_d_type': 'after',  # which part of r_f_d to use
            'rgb_start': [0.4, 0.45],  #
            'rgb_theta_diff_c': 1,
            'rgb_v_diff_c': 0.01,
            'sp_len_loc': 5, 'sp_len_scale': 15,
            'ld': [_s.ld[0] - 0, _s.ld[1] + 15],
            'ld_offset_loc': [0, 2],
            'ld_offset_scale': [1, 1],
            'R_ss': [0.8, 1], 'R_scale': 0.2,
            'G_ss': [0.4, 0.2], 'G_scale': 0.2,
            'B_ss': [0.1, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'alpha_y_range': [0.01, 0.9],
            'up_down': 'down'
        }

        # 160, 77, 36  -> 76, 42, 28

        return sps_gi





