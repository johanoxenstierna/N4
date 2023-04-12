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
        _s.child_names = ['sps', 'ls', 'rs', 'srs']

        '''THIS IS SHIT: Basically they will only be plotted once so they will be unavailable for 99% of init_frames, 
        but sps plotted a bunch.
        NEW: Only plotted once and sps controlled with init_frame_max_dist and num_scale
        '''
        _s.zorder = 130
        _s.ls_gi = _s.gen_ls_gi(pulse)  # NO DYN_GEN

        if P.A_SPS:

            '''
            TODO distribute these between them based on pulse. 
            TODO2: add num sp to generate (50 in main) whenever init frame hit
            L needs to be generated based on these. 
            '''

            # sps_init_frames = []
            # _s.sps_gi0, sps_init_frames = _s.gen_sps_gi0(sps_init_frames)
            # _s.sps_gi1, sps_init_frames = _s.gen_sps_gi1(sps_init_frames)\

            init_frames_sp0 = [pulse[0] - 100]
            init_frames_sp1 = [pulse[1] - 100, pulse[1], pulse[1] + 100]  # 150 is init_frame_max_dist
            init_frames_sp2 = [pulse[2] - 100, pulse[2], pulse[2] + 100]  # 150 is init_frame_max_dist
            init_frames_sp3 = [pulse[3] - 100, pulse[3], pulse[3] + 100]  # 150 is init_frame_max_dist

            _s.sps_gi0 = _s.gen_sps_gi0(init_frames_sp0)
            _s.sps_gi1 = _s.gen_sps_gi1(init_frames_sp1)
            _s.sps_gi2 = _s.gen_sps_gi2(init_frames_sp2)
            _s.sps_gi3 = _s.gen_sps_gi3(init_frames_sp3)

            _s.sps_gi = {
                '0': _s.sps_gi0,
                '1': _s.sps_gi1,
                '2': _s.sps_gi2,
                '3': _s.sps_gi3
            }
            # sps_init_frames.sort()
            # _s.sps_gi_init_frames = init_frames_sp0 + init_frames_sp1 + init_frames_sp2 + init_frames_sp3

            lol = [val['init_frames'] for key, val in _s.sps_gi.items()]
            lol = [x for sublist in lol for x in sublist]
            lol.sort(reverse=False)
            _s.sps_gi_init_frames = lol

            '''
            flat_list = []
            for sublist in lol:
                for item in sublist:
                    flat_list.append(item)
                    
             for sublist in lol: for item in sublist: yield item
            '''

        if P.A_SRS:
            '''HAVE TO STAY SEPARATED BCS TIED TO LS INIT FRAMES AND LD. 
            SOME REDUNDANCY BCS EVERYTHING ELSE IS SAME BUT WHATEVER'''
            _s.srs_gi0 = _s.gen_srs_gi0()
            _s.srs_gi1 = _s.gen_srs_gi1()
            _s.srs_gi2 = _s.gen_srs_gi2()
            _s.srs_gi3 = _s.gen_srs_gi3()

            _s.srs_gi = {  # these numbers correspond to c!
                '0': _s.srs_gi0,
                '1': _s.srs_gi1,
                '2': _s.srs_gi2,
                '3': _s.srs_gi3
            }

            _s.srs_gi_init_frames = [val['init_frames'] for key, val in _s.srs_gi.items()]
            _s.srs_gi_init_frames = list(np.asarray(_s.srs_gi_init_frames).flatten())

        if P.A_RS:
            # rs_init_frames = random.sample(range(pulse[0], pulse[-1]), min(50, len(pulse)))

            '''TEMEEEEMP'''
            rs_init_frames = random.sample(range(min(pulse), max(pulse)), min(50, len(pulse)))
            _s.rs_gi = _s.gen_rs_gi(rs_init_frames)

    def gen_ls_gi(_s, pulse):

        """
        SHARED FOR THE SAME SH. Kind of... makes sense. ld is used for extent, but they are modified
        for each l in l class finish info.
        """

        # lif0, lif1 = _s.distribute_pulse_for_ls(pulse)  # l_init_frame
        lif0 = [pulse[0]]
        lif1 = [pulse[1]]
        lif2 = [pulse[2]]
        lif3 = [pulse[3]]
        l_init_frames = lif0 + lif1 + lif2 + lif3

        l_gi = {
            'init_frames_all': l_init_frames,
            'lif0': lif0,
            'lif1': lif1,
            'lif2': lif2,
            'lif3': lif3,
            'frames_tot0': 150,
            'frames_tot1': 500,
            'frames_tot2': 500,
            'frames_tot3': 500,
            'ld': _s.ld,  # USED BY SR?
            'ld0': [_s.ld[0] - 11, _s.ld[1] + 23],
            'ld1': [_s.ld[0] - 27, _s.ld[1] + 45],
            'ld2': [_s.ld[0] - 65, _s.ld[1] + 72],
            'ld3': [_s.ld[0] - 20, _s.ld[1] + 52],
            'scale': 0.5,
            'frame_ss': _s.frame_ss,
            'zorder': 200  # 3 is 110
        }

        return l_gi

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


        # BELOW IS TOO BRITTLE
        # for i in range(len(_s.ls_gi['lif0'])):
        #     init_frame_sp = max(10,  _s.ls_gi['lif0'][i] - 100)  # OBS first number needs to be different for each sp
        #     if init_frame_sp in init_frames:
        #         raise Exception("cs sp init_frame already exists. COULD BE THAT INIT_FRAMES NEED TO BE DELAYED")
        #     else:
        #         init_frames_sp.append(init_frame_sp)
        #         init_frames.append(init_frame_sp)

        sps_gi = {
            'gi_id': '0',
            'init_frames': init_frames_sp,
            'frames_tot': 200,  # NEEDS TO MATCH WITH EXPL ???
            'init_frame_max_dist': 100,  # OBS THIS MUST BE SHORTER
            'v_loc': 80, 'v_scale': 12,
            # 'num_loc': P.NUM_SPS_L, 'num_scale': P.NUM_SPS_L / 2,
            'theta_loc': -1.1, 'theta_scale': 0.05,  # neg is left  with straight down= -1.6, 0=
            'r_f_d_loc': 0.1, 'r_f_d_scale': 0.02,
            'r_f_d_type': 'after',  # which part of r_f_d to use
            'sp_len_loc': 5, 'sp_len_scale': 5,
            'rgb_start': [0.4, 0.9],  #
            'rgb_theta_diff_c': 1,
            'rgb_v_diff_c': 0.01,
            'ld': [_s.ld[0] + 3, _s.ld[1] - 5],  # NOT TIED TO L BCS TUNING NEEDED ANYWAY
            'ld_offset_loc': [0, 2],
            'ld_offset_scale': [0, 0.01],
            'R_ss': [0.9, 1], 'R_scale': 0.2,
            'G_ss': [0.5, 0.2], 'G_scale': 0.15,
            'B_ss': [0.2, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'alpha_y_range': [0.01, 0.5],
            'up_down': 'down'
        }

        return sps_gi

    def gen_srs_gi0(_s):
        """ARE PICS SELECTED RANDOMLY"""

        init_frames = []
        for i in range(-10, 10, 3):  # 5 total for each ls
            init_frame = _s.ls_gi['lif0'][0] + i
            init_frames.append(init_frame)

        srs_gi = {
            # 'l_id': 0,  # a position in a list
            'init_frames': init_frames,
            'ld': _s.ls_gi['ld0'],
            'ld_offset_loc': [0, 0],  # THIS IS WRT ld0!
            'ld_offset_scale': [1, 3],  # OBS there is no ss, only start!
            'frames_tot': 200,
            'v_loc': 10,  # rc=2
            'v_scale': 2,
            'scale_ss': [0.01, 3],
            'theta_loc': -0.9,  # 0.6 * 2 * np.pi,  # 2pi and pi are both straight up
            'theta_scale': 0.0,
            'rad_rot': -0.3,
            'r_f_d_loc': 0.05,
            'r_f_d_scale': 0.00,
            'up_down': 'up',
            'alpha_y_range': [0.01, 0.2],
            'zorder': _s.zorder + 10
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

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
            'ld_offset_scale': [0, 0.1],
            'R_ss': [0.8, 1], 'R_scale': 0.2,
            'G_ss': [0.4, 0.2], 'G_scale': 0.2,
            'B_ss': [0.1, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'alpha_y_range': [0.05, 0.5],
            'up_down': 'down'
        }

        # 160, 77, 36  -> 76, 42, 28

        return sps_gi

    def gen_srs_gi1(_s):

        # in_f, init_frames, frames_tot = _s.gen_srs_init_frames(_cs_gi=_s.cs_gi0, init_frames=init_frames_sr0)

        # assert (in_f[-1] < P.FRAMES_STOP)

        init_frames = []
        for i in range(-10, 10, 3):  # 5 total for each ls
            init_frame = _s.ls_gi['lif1'][0] + i
            init_frames.append(init_frame)

        srs_gi = {
            # 'l_id': 1,  # a position in a list
            'init_frames': init_frames,
            'ld': _s.ls_gi['ld1'],
            'ld_offset_loc': [0, 0],  # OBS there is no ss, only start!
            'ld_offset_scale': [1, 3],  # OBS there is no ss, only start!
            'frames_tot': 200,
            'v_loc': 10,  # rc=2
            'v_scale': 2,
            'scale_ss': [0.01, 4],
            'theta_loc': -0.9,  # 0.6 * 2 * np.pi,  # 2pi and pi are both straight up
            'theta_scale': 0.0,
            'rad_rot': -0.3,
            'r_f_d_loc': 0.05,
            'r_f_d_scale': 0.00,
            'up_down': 'up',
            'alpha_y_range': [0, 0.2],
            'zorder': _s.zorder + 10
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

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
            'frames_tot': 250,
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
            'ld_offset_scale': [0, 0.1],
            'R_ss': [0.8, 1], 'R_scale': 0.2,
            'G_ss': [0.4, 0.2], 'G_scale': 0.2,
            'B_ss': [0.1, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'alpha_y_range': [0.05, 0.5],
            'up_down': 'down'
        }

        # 160, 77, 36  -> 76, 42, 28

        return sps_gi

    def gen_srs_gi2(_s):

        # in_f, init_frames, frames_tot = _s.gen_srs_init_frames(_cs_gi=_s.cs_gi0, init_frames=init_frames_sr0)

        # assert (in_f[-1] < P.FRAMES_STOP)

        init_frames = []
        for i in range(-10, 10, 3):  # 5 total for each ls
            init_frame = _s.ls_gi['lif2'][0] + i
            init_frames.append(init_frame)

        srs_gi = {
            # 'l_id': 2,  # a position in a list
            'init_frames': init_frames,
            'ld': _s.ls_gi['ld2'],
            'ld_offset_loc': [0, 0],  # OBS there is no ss, only start!
            'ld_offset_scale': [1, 3],  # OBS there is no ss, only start!
            'frames_tot': 200,
            'v_loc': 10,  # rc=2
            'v_scale': 2,
            'scale_ss': [0.01, 3],
            'theta_loc': -0.9,  # 0.6 * 2 * np.pi,  # 2pi and pi are both straight up
            'theta_scale': 0.0,
            'rad_rot': -0.3,
            'r_f_d_loc': 0.05,
            'r_f_d_scale': 0.00,
            'up_down': 'up',
            'alpha_y_range': [0, 0.2],
            'zorder': _s.zorder + 10
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

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
            'frames_tot': 250,
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
            'ld_offset_scale': [0.1, 0.1],
            'R_ss': [0.8, 1], 'R_scale': 0.2,
            'G_ss': [0.4, 0.2], 'G_scale': 0.2,
            'B_ss': [0.1, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'alpha_y_range': [0.01, 0.9],
            'up_down': 'down'
        }

        # 160, 77, 36  -> 76, 42, 28

        return sps_gi

    def gen_srs_gi3(_s):

        # in_f, init_frames, frames_tot = _s.gen_srs_init_frames(_cs_gi=_s.cs_gi0, init_frames=init_frames_sr0)

        # assert (in_f[-1] < P.FRAMES_STOP)

        init_frames = []
        for i in range(-10, 10, 3):  # 5 total for each ls
            init_frame = _s.ls_gi['lif3'][0] + i
            init_frames.append(init_frame)

        srs_gi = {
            # 'l_id': 3,  # a position in a list
            'init_frames': init_frames,
            'ld': _s.ls_gi['ld3'],
            'ld_offset_loc': [0, 0],  # OBS there is no ss, only start!
            'ld_offset_scale': [1, 3],  # OBS there is no ss, only start!
            'frames_tot': 200,
            'v_loc': 10,  # rc=2
            'v_scale': 2,
            'scale_ss': [0.01, 4],
            'theta_loc': -0.9,  # 0.6 * 2 * np.pi,  # 2pi and pi are both straight up
            'theta_scale': 0.0,
            'rad_rot': -0.3,
            'r_f_d_loc': 0.05,
            'r_f_d_scale': 0.00,
            'up_down': 'up',
            'alpha_y_range': [0, 0.2],
            'zorder': _s.zorder + 10
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

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
