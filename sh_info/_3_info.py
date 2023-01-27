import copy

from sh_info.shInfoAbstract import ShInfoAbstract
import P as P
import random
import numpy as np


class Sh_3_info(ShInfoAbstract):
    """
    Basically this is the json replacement (also chronicle to some extent).
    Just very basic stuff
    """

    def __init__(_s, pulse, top_point):
        super().__init__()
        _s.id = '3'
        _s.extent = "static"
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]  # ONLY ONE WHO USES .
        _s.zorder = 10

        _s.ld = [top_point[0] + 0, top_point[1] + 0]
        _s.child_names = ['cs', 'srs', 'sps']  # both cks and cds

        _s.num_sp_at_init_frame = 50

        if P.A_CS:  # THEY ALL HAVE INDIVIDUAL GI'S
            _s.cs_gi0 = _s.gen_cs_gi0()
            _s.cs_gi1 = _s.gen_cs_gi1()
            # _s.cs_gi2 = _s.gen_cs_gi2()
            # _s.cs_gi3 = _s.gen_cs_gi3()
            # _s.cs_gi10 = _s.gen_cs_gi10()

        if P.A_SRS:  # different gis here have nothing to do with pic, but rather with init frames

            '''INIT_FRAMES MUST BE UNIQUE. ALSO, ONCE ADDED, IT WILL BE PARSED IN MAIN, 
            AND WILL CRASH IF THERE IS NO CORRESPONDING C PIC'''
            init_frames = []

            '''remove to not show'''
            _s.srs_gi0, init_frames = _s.gen_srs_gi0(init_frames)  # THIS MEANS THERE MUST BE A '3_c_0'
            _s.srs_gi1, init_frames = _s.gen_srs_gi1(init_frames)
            # _s.srs_gi2, init_frames = _s.gen_srs_gi2(init_frames)  # perhaps redundant

            _s.srs_gi = {  # these numbers correspond to c!
                '0': _s.srs_gi0,
                '1': _s.srs_gi1  # IF A C AND CORR SR EXISTS, THEN SO MUST THIS
                # '2': _s.srs_gi2
            }
            _s.srs_gi_init_frames = init_frames

        if P.A_SPS:

            '''
            OBS sps_gi0 and sps_gi1 CAN BE CALLED BY ANY SH, SO NAME CANT BE CHANGED
            '''



            init_frames = []  # NEW: EACH GI ONLY HAS 1 INIT_FRAME, BUT THEY STILL CANT BE SAME.
            _s.sps_gi0 = _s.gen_sps_gi0()  # THIS MEANS THERE MUST BE A '3_c_0'
            # _s.sps_gi0['init_frames'] = [10, 50, 70, 100, 250]  # THIS CAUSES IT
            # assert(10 + _s.sps_gi0['frames_tot'] + 100 < P.FRAMES_STOP)

            _s.sps_gi2 = _s.gen_sps_gi2()
            # _s.sps_gi2['init_frames'] = [30, 100, 150, 200]
            # assert(40 + _s.sps_gi2['frames_tot'] + 100 < P.FRAMES_STOP)

            _s.sps_gi10, init_frames = _s.gen_sps_gi10(init_frames)

            # _s.sps_init_frames = _s.sps_gi0['init_frames'] + _s.sps_gi2['init_frames']
            _s.sps_init_frames = init_frames
            _s.sps_init_frames.sort()

        aa = 5

    def gen_srs_init_frames(_s, _cs_gi, init_frames):

        frames_tot = 200
        if P.DEBUG:
            frames_tot = 140
        clf = _cs_gi['init_frame'] + _cs_gi['frames_tot'] + _cs_gi['frames_tot1']  # c_last_frame
        start = _cs_gi['init_frame'] + int(_cs_gi['frames_tot']/2)
        stop = clf + 5
        in_f = list(range(start, stop, 4))
        in_f2 = []

        # attempts = 200
        # fl_found_fr = False
        # while fl_found_fr == False:

        for fr in in_f:
            if fr not in init_frames:
                in_f2.append(fr)
                init_frames.append(fr)
            else:
                print("sr frame already occupied! " + str(fr) + _cs_gi.__class__.__name__)
                raise Exception("better to fix this now.")
        in_f = in_f2

        return in_f, init_frames, frames_tot

    def gen_cs_gi0(_s, _type=None, init_frame=2):

        ld = [_s.ld[0] - 10, _s.ld[1] + 10]

        frames_tot = 30
        frames_tot1 = 50

        if P.DEBUG:
            frames_tot = 10
            frames_tot1 = 30

        frame_ss = [init_frame + frames_tot, init_frame + frames_tot + frames_tot1]

        gi = {
            'init_frame': init_frame,
            'ld': ld,
            'frames_tot': frames_tot,
            'frames_tot1': frames_tot1,
            'frame_ss': frame_ss,
            'scale_ss': [1, 1],
            'v': 12,
            'theta': 2,
            'r_f_d': 0.01,
            'extra_offset_x': 0,
            'extra_offset_y': 0,
            'up_down': 'up',
            'rad_rot': -1,
            'zorder': 110
        }

        # gi['init_frame'] = 2
        # gi['ld'] = [_s.ld[0] - 12, _s.ld[1] + 10]  # -6 TUNED WITH affine2D.translate!!!
        # gi['frames_tot'] = 10
        # gi['frames_tot1'] = 100
        #
        # if P.DEBUG:
        #     gi['frames_tot'] = 10
        #     gi['frames_tot1'] = 20
        #
        # '''OBS THIS HAS TO BE SECOND BEFORE SET_EXTENT, THEN SET TO FIRST'''
        # # gi['ld_ss'] = [[gi['ld'][0], gi['ld'][1]], [gi['ld'][0], gi['ld'][1]]]  # set extent needs this
        # gi['frame_ss'] = [gi['init_frame'], gi['init_frame'] + gi['frames_tot']]
        # gi['frame_ss'] = [gi['frame_ss'][1], gi['frame_ss'][1] + gi['frames_tot1']]
        # # gi['frame_ss1'] = [gi['frame_ss'][1], gi['frame_ss'][1] + 30]
        # gi['scale_ss'] = [1, 1]
        #
        # gi['v'] = 20
        # gi['theta'] = 0.8 * 2 * np.pi   # 2pi/4 is straight up, 2pi/8 is 45% to right   pos=left, neg=right
        # # gi['theta'] = np.pi + 0.001  # 2pi/4 is straight up, 2pi/8 is 45% to right
        # gi['r_f_d'] = 0.01  # THIS MESSES UP START POS
        # gi['extra_offset_x'] = 0
        # gi['extra_offset_y'] = 5
        # gi['up_down'] = 'up'
        #
        # gi['zorder'] = 110

        '''cd'''

        return gi

    def gen_srs_gi0(_s, init_frames):
        """
        OBS controls movement of ALL srs for a GIVEN c.
        """

        in_f, init_frames, frames_tot = _s.gen_srs_init_frames(_cs_gi=_s.cs_gi0, init_frames=init_frames)

        assert(in_f[-1] < P.FRAMES_STOP)

        srs_gi = {
            'c_id': '3_c_0',
            'init_frames': in_f,
            'ld_offset_loc': [5, 0],  # OBS there is no ss, only start!
            'ld_offset_scale': [1, 3],  # OBS there is no ss, only start!
            'frames_tot': frames_tot,
            'v_loc': 100,  # rc=2
            'v_scale': 4,
            'theta_loc': -0.5,  #0.6 * 2 * np.pi,  # 2pi and pi are both straight up
            'theta_scale': 0.0,
            'r_f_d_loc': 0.5,
            'r_f_d_scale': 0.00,
            'up_down': 'down',
            'zorder': _s.cs_gi0['zorder']
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi, init_frames

    def gen_cs_gi1(_s, _type=None, init_frame=2):
        gi = {}

        '''ck'''

        ld = [_s.ld[0] - 50, _s.ld[1] + 40]

        frames_tot = 60
        frames_tot1 = 210

        if P.DEBUG:
            frames_tot = 30
            frames_tot1 = 50

        frame_ss = [init_frame + frames_tot, init_frame + frames_tot + frames_tot1]

        gi = {
            'init_frame': init_frame,
            'ld': ld,
            'frames_tot': frames_tot,
            'frames_tot1': frames_tot1,
            'frame_ss': frame_ss,
            'scale_ss': [1, 1],
            'v': 20,
            'theta': 2,
            'r_f_d': 0.1,
            'extra_offset_x': 0,
            'extra_offset_y': 5,
            'up_down': 'up',
            'rad_rot': 0.5,
            'zorder': 110
        }

        # gi['init_frame'] = 2
        # gi['ld'] = [_s.ld[0] - 50, _s.ld[1] + 40]  # -6 TUNED WITH affine2D.translate!!!
        # # gi['ld'] = [_s.ld[0] - 13, _s.ld[1] + 3]  # -6 TUNED WITH affine2D.translate!!!
        #
        # gi['frames_tot'] = 60
        # gi['frames_tot1'] = 210
        #
        # if P.DEBUG:
        #     gi['frames_tot'] = 30
        #     gi['frames_tot1'] = 50
        #
        # # frame_ss =
        #
        # '''OBS THIS HAS TO BE SECOND BEFORE SET_EXTENT, THEN SET TO FIRST'''
        # # gi['ld_ss'] = [[gi['ld'][0], gi['ld'][1]], [gi['ld'][0], gi['ld'][1]]]  # set extent needs this
        # gi['frame_ss'] = [gi['init_frame'], gi['init_frame'] + gi['frames_tot']]
        # gi['frame_ss'] = [gi['frame_ss'][1], gi['frame_ss'][1] + gi['frames_tot1']]
        # # gi['frame_ss1'] = [gi['frame_ss'][1], gi['frame_ss'][1] + 30]
        # gi['scale_ss'] = [1, 1]
        #
        # gi['v'] = 25
        # gi['theta'] = 0.8 * 2 * np.pi   # 2pi/4 is straight up, 2pi/8 is 45% to right   pos=left, neg=right
        # # gi['theta'] = np.pi + 0.001  # 2pi/4 is straight up, 2pi/8 is 45% to right
        # gi['r_f_d'] = 0.01  # THIS MESSES UP START POS
        # gi['extra_offset_x'] = 0
        # gi['extra_offset_y'] = 8
        # gi['up_down'] = 'up'
        # gi['zorder'] = 90

        '''cd'''

        return gi

    def gen_srs_gi1(_s, init_frames):
        """
        OBS only shown ONCE. DONT WORRY ABOUT MEM THESE PICS ARE TINY
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        20 sr total init_frames per c.
        """

        in_f, init_frames, frames_tot = _s.gen_srs_init_frames(_cs_gi=_s.cs_gi1, init_frames=init_frames)

        srs_gi = {
            'c_id': '3_c_1',
            'init_frames': in_f,
            'ld_offset_loc': [23, -20],  # OBS there is no ss, only start!
            'ld_offset_scale': [6, 2],  # OBS there is no ss, only start!
            'frames_tot': frames_tot,
            'v_loc': 120,  # rc=2
            'v_scale': 6,
            'theta_loc': -0.5, #0.9 * 2 * np.pi,  # 2pi and pi are both straight up
            'theta_scale': 0.000,
            'r_f_d_loc': 0.5,
            'r_f_d_scale': 0.05,
            'up_down': 'down',
            'zorder': _s.cs_gi1['zorder']
        }

        return srs_gi, init_frames

    def gen_cs_gi2(_s, _type=None):
        gi = {}

        '''ck'''
        gi['init_frame'] = 2
        gi['ld'] = [_s.ld[0] - 40, _s.ld[1] + 30]  # -6 TUNED WITH affine2D.translate!!!
        # gi['ld'] = [_s.ld[0] - 13, _s.ld[1] + 3]  # -6 TUNED WITH affine2D.translate!!!

        gi['frames_tot'] = 30
        gi['frames_tot1'] = 200

        if P.DEBUG:
            gi['frames_tot'] = 20
            gi['frames_tot1'] = 40

        '''OBS THIS HAS TO BE SECOND BEFORE SET_EXTENT, THEN SET TO FIRST'''
        gi['ld_ss'] = [[gi['ld'][0], gi['ld'][1]], [gi['ld'][0], gi['ld'][1]]]  # set extent needs this
        gi['frame_ss'] = [gi['init_frame'], gi['init_frame'] + gi['frames_tot']]
        gi['frame_ss'] = [gi['frame_ss'][1], gi['frame_ss'][1] + gi['frames_tot1']]
        # gi['frame_ss1'] = [gi['frame_ss'][1], gi['frame_ss'][1] + 30]
        gi['scale_ss'] = [1, 1]

        gi['v'] = 15
        gi['theta'] = 0.8 * 2 * np.pi   # 2pi/4 is straight up, 2pi/8 is 45% to right   pos=left, neg=right
        # gi['theta'] = np.pi + 0.001  # 2pi/4 is straight up, 2pi/8 is 45% to right
        gi['r_f_d'] = 0.01  # THIS MESSES UP START POS
        gi['extra_offset_x'] = 0
        gi['extra_offset_y'] = 8
        gi['up_down'] = 'up'

        gi['zorder'] = 90

        '''cd'''

        return gi

    def gen_srs_gi2(_s, init_frames):
        """
        OBS only shown ONCE. DONT WORRY ABOUT MEM THESE PICS ARE TINY
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        20 sr total init_frames per c.
        """

        in_f, init_frames, frames_tot = _s.gen_srs_init_frames(_cs_gi=_s.cs_gi2, init_frames=init_frames)

        srs_gi = {
            'c_id': '3_c_2',
            'init_frames': in_f,
            'ld_offset_loc': [5, 1],  # OBS there is no ss, only start!
            'ld_offset_scale': [4, 5],  # OBS there is no ss, only start!
            'frames_tot': frames_tot,
            'v_loc': 5,  # rc=2
            'v_scale': 2,
            'theta_loc': 0.6 * 2 * np.pi,  # 2pi and pi are both straight up
            'theta_scale': 0.0,
            'r_f_d_loc': 0.1,
            'r_f_d_scale': 0.00,
            'up_down': 'up',
            'zorder': _s.cs_gi2['zorder']
        }

        return srs_gi, init_frames

    def gen_cs_gi3(_s, _type=None):
        gi = {}

        '''ck'''
        gi['init_frame'] = 2
        gi['ld'] = [_s.ld[0] - 10, _s.ld[1] + 8]  # -6 TUNED WITH affine2D.translate!!!
        # gi['ld'] = [_s.ld[0] - 13, _s.ld[1] + 3]  # -6 TUNED WITH affine2D.translate!!!

        gi['frames_tot'] = 30
        gi['frames_tot1'] = 200

        if P.DEBUG:
            gi['frames_tot'] = 30
            gi['frames_tot1'] = 50

        '''OBS THIS HAS TO BE SECOND BEFORE SET_EXTENT, THEN SET TO FIRST'''
        gi['ld_ss'] = [[gi['ld'][0], gi['ld'][1]], [gi['ld'][0], gi['ld'][1]]]  # set extent needs this
        gi['frame_ss'] = [gi['init_frame'], gi['init_frame'] + gi['frames_tot']]
        gi['frame_ss'] = [gi['frame_ss'][1], gi['frame_ss'][1] + gi['frames_tot1']]
        # gi['frame_ss1'] = [gi['frame_ss'][1], gi['frame_ss'][1] + 30]
        gi['scale_ss'] = [1, 1]

        gi['v'] = 15
        gi['theta'] = 0.8 * 2 * np.pi   # 2pi/4 is straight up, 2pi/8 is 45% to right   pos=left, neg=right
        # gi['theta'] = np.pi + 0.001  # 2pi/4 is straight up, 2pi/8 is 45% to right
        gi['r_f_d'] = 0.01  # THIS MESSES UP START POS
        gi['extra_offset_x'] = 0
        gi['extra_offset_y'] = 8
        gi['up_down'] = 'up'

        gi['zorder'] = 90

        '''cd'''

        return gi

    def gen_cs_gi10(_s, _type=None):
        gi = {}

        '''ck'''
        gi['init_frame'] = 7
        gi['ld'] = [_s.ld[0] + 15, _s.ld[1] + 8]  # -6 TUNED WITH affine2D.translate!!!
        # gi['ld'] = [_s.ld[0] - 13, _s.ld[1] + 3]  # -6 TUNED WITH affine2D.translate!!!

        gi['frames_tot'] = 40
        gi['frames_tot1'] = 190

        if P.DEBUG:
            gi['frames_tot'] = 10
            gi['frames_tot1'] = 20

        '''OBS THIS HAS TO BE SECOND BEFORE SET_EXTENT, THEN SET TO FIRST'''
        gi['ld_ss'] = [[gi['ld'][0], gi['ld'][1]], [gi['ld'][0], gi['ld'][1]]]  # set extent needs this
        gi['frame_ss'] = [gi['init_frame'], gi['init_frame'] + gi['frames_tot']]
        gi['frame_ss'] = [gi['frame_ss'][1], gi['frame_ss'][1] + gi['frames_tot1']]
        # gi['frame_ss1'] = [gi['frame_ss'][1], gi['frame_ss'][1] + 30]
        gi['scale_ss'] = [1, 1]

        gi['v'] = 15
        gi['theta'] = -0.3 * 2 * np.pi   # 2pi/4 is straight up, 2pi/8 is 45% to right   pos=left, neg=right
        # gi['theta'] = np.pi + 0.001  # 2pi/4 is straight up, 2pi/8 is 45% to right
        gi['r_f_d'] = 0.01  # THIS MESSES UP START POS
        gi['extra_offset_x'] = -1
        gi['extra_offset_y'] = 3
        gi['up_down'] = 'up'

        gi['zorder'] = 120

        '''cd'''

        return gi

    def gen_sps_gi0(_s):

        """
        top left one
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)

        OBS init_frame is set as random.randint(0, 100) in dyn_gen() SHOULD BE MOVED HERE.

        """

        clf = _s.cs_gi0['init_frame'] + _s.cs_gi0['frames_tot'] + _s.cs_gi0['frames_tot1']  # c_last_frame

        sps_gi = {
            'init_frames': [clf],
            'gi_id': '0',
            'frames_tot': 150,
            'init_frame_max_dist': 5,
            'v_loc': 140, 'v_scale': 5,
            'num_loc': P.NUM_SPS_F, 'num_scale': P.NUM_SPS_F / 2,
            'theta_loc': -0.2, 'theta_scale': 0.3,
            'r_f_d_loc': 0.2, 'r_f_d_scale': 0.05,
            'r_f_d_type': 'after',  # which part of r_f_d to use
            'ld': _s.ld,
            'ld_offset_loc': [0, 1],
            'ld_offset_scale': [0, 0.1],
            'R_ss': [0.9, 1], 'R_scale': 0,
            'G_ss': [0.5, 0.01], 'G_scale': 0.1,
            'B_ss': [0.01, 0.01], 'B_scale': 0,  # good to prevent neg numbers here
            'up_down': 'up'
        }

        return sps_gi

    def gen_sps_gi2(_s):

        """
        lower left one
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)
        """

        clf = _s.cs_gi2['init_frame'] + _s.cs_gi2['frames_tot'] + _s.cs_gi2['frames_tot1']  # c_last_frame

        sps_gi = {
            'init_frames': [clf],
            'gi_id': '2',
            'frames_tot': 230,
            'init_frame_max_dist': 5,  # random num of frames in future from init frame
            'v_loc': 180, 'v_scale': 10,
            'num_loc': P.NUM_SPS_SH, 'num_scale': P.NUM_SPS_SH / 2,
            'theta_loc': 0.8, 'theta_scale': 0.07,
            'r_f_d_loc': 0.1, 'r_f_d_scale': 0.05,
            'r_f_d_type': 'after',  # which part of r_f_d to use
            'ld': _s.ld,
            'ld_offset_loc': [-4, 5],
            'ld_offset_scale': [0, 0],
            'R_ss': [0.8, 0.9], 'R_scale': 0.2,
            'G_ss': [0.8, 0.2], 'G_scale': 0.1,
            'B_ss': [0.7, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'up_down': 'up'

        }

        return sps_gi

    def gen_sps_gi10(_s, init_frames):

        """
        lower left one
        THESE ARE AVERAGES
        r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
        climb up the projectile (before shifting)
        """

        clf = _s.cs_gi10['init_frame'] + _s.cs_gi10['frames_tot'] + _s.cs_gi10['frames_tot1']  # c_last_frame

        init_frames.append(clf)

        sps_gi = {
            '_type': 'sp_c',
            'init_frames': [clf],
            'gi_id': '10',
            'frames_tot': 230,
            'init_frame_max_dist': 5,  # random num of frames in future from init frame
            'v_loc': 30, 'v_scale': 10,
            'num_loc': P.NUM_SPS_SH, 'num_scale': P.NUM_SPS_SH / 2,
            'theta_loc': -0.2, 'theta_scale': 0.01,
            'r_f_d_loc': 0.5, 'r_f_d_scale': 0.05,
            'r_f_d_type': 'after',  # which part of r_f_d to use
            'ld': _s.ld,
            'ld_offset_loc': [20, 30],
            'ld_offset_scale': [0, 0],
            'R_ss': [0.8, 0.9], 'R_scale': 0.2,
            'G_ss': [0.8, 0.2], 'G_scale': 0.1,
            'B_ss': [0.7, 0.05], 'B_scale': 0.01,  # good to prevent neg numbers here
            'up_down': 'up'

        }

        return sps_gi, init_frames