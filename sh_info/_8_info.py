
from sh_info.shInfoAbstract import ShInfoAbstract
import P as P
import random
import numpy as np
import copy

class Sh_8_info(ShInfoAbstract):
    """
    Extras. For now try to do just 1 at init_frame with low alpha.
    Basically this is the json replacement (also chronicle to some extent).
    Just very basic stuff
    """

    def __init__(_s, top_point):
        super().__init__()
        _s.id = '8'
        _s.extent = "static"
        _s.child_names = ['srs']
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.ld = top_point

        # pulse_srs = _s.gen_pulse_srs8(pulse)  # NAW: easier to set it for each
        _s.srs_gi = {  # THESE NEED SEPARATION MAINLY BCS OF INIT FRAMES
            '0': _s.gen_srs_gi0(),
            '1': _s.gen_srs_gi1(),
            '2': _s.gen_srs_gi2(),
            '3': _s.gen_srs_gi3(),
            '4': _s.gen_srs_gi4(),
            '5': _s.gen_srs_gi5(),
            '6': _s.gen_srs_gi6(),
            '7': _s.gen_srs_gi7(),
            '8': _s.gen_srs_gi8()
        }
        # _s.srs_gi_init_frames = _s.srs_gi['4']['init_frames']
        _s.srs_gi_init_frames = [val['init_frames'] for key, val in _s.srs_gi.items()]
        _s.srs_gi_init_frames = list(np.asarray(_s.srs_gi_init_frames).flatten())

        _s.zorder = None  # set from gi

    def gen_srs_gi0(_s):

        srs_gi = {
            'id': 0,
            'init_frames': [10, 20, 30, 40, 50],
            'frames_tot': 300,
            'v_linear_loc': [-0.3, 0],
            'v_linear_scale': [0.1, 0.02],
            'ld': _s.ld,  # finish_info
            'ld_offset_loc': [-100, -15],
            'ld_offset_scale': [1, 1],
            'scale_ss': [1, 1],  # assumed big pics
            'rad_rot': random.uniform(-0.1, -0.3),
            'alpha_y_range': [0.1, 0.2],
            'up_down': None,  # key checked for alpha
            'zorder': 90,
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_srs_gi1(_s):
        srs_gi = {
            'id': 1,
            'init_frames': [11, 21, 31, 41, 51],
            'frames_tot': 300,
            'v_linear_loc': [-0.3, 0],
            'v_linear_scale': [0.15, 0.02],
            'ld': _s.ld,  # finish_info
            'ld_offset_loc': [-60, -5],
            'ld_offset_scale': [1, 1],
            'scale_ss': [1, 1],  # assumed big pics
            'rad_rot': random.uniform(-0.1, -0.3),
            'alpha_y_range': [0.1, 0.3],
            'up_down': None,  # key checked for alpha
            'zorder': 90,
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_srs_gi2(_s):
        srs_gi = {
            'id': 2,
            'init_frames': [12, 22, 32, 42, 52],
            'frames_tot': 300,
            'v_linear_loc': [-0.3, 0],
            'v_linear_scale': [0.1, 0.02],
            'ld': _s.ld,  # finish_info
            'ld_offset_loc': [-100, 5],
            'ld_offset_scale': [1, 1],
            'scale_ss': [1, 1],  # assumed big pics
            'rad_rot': random.uniform(-0.1, -0.3),
            'alpha_y_range': [0.7, 1],
            'up_down': None,  # key checked for alpha
            'zorder': 90,
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_srs_gi3(_s):
        srs_gi = {
            'id': 3,
            'init_frames': [13, 23, 33, 43, 53],
            'frames_tot': 300,
            'v_linear_loc': [-0.3, 0],
            'v_linear_scale': [0.15, 0.02],
            'ld': _s.ld,  # finish_info
            'ld_offset_loc': [10, 5],
            'ld_offset_scale': [1, 1],
            'scale_ss': [1, 1],  # assumed big pics
            'rad_rot': random.uniform(-0.1, -0.3),
            'alpha_y_range': [0.1, 0.3],
            'up_down': None,  # key checked for alpha
            'zorder': 90,
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_srs_gi4(_s):

        srs_gi = {
            'id': 4,
            'init_frames': [14, 24, 34, 44, 54],
            'frames_tot': 600,
            'v_linear_loc': [-0.3, 0],
            'v_linear_scale': [0.02, 0.01],
            'ld': _s.ld,  # finish_info
            'ld_offset_loc': [-50, 50],
            'ld_offset_scale': [1, 1],
            'scale_ss': [1, 1],  # assumed big pics
            'rad_rot': random.uniform(-0.1, -0.2),
            'alpha_y_range': [0.01, 0.3],
            'up_down': None,  # key checked for alpha
            'zorder': 200,
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_srs_gi5(_s):

        srs_gi = {
            'id': 5,
            'init_frames': [25, 35, 45, 55, 65],
            'frames_tot': 600,
            'v_linear_loc': [-0.3, 0],
            'v_linear_scale': [0.02, 0.01],
            'ld': _s.ld,  # finish_info
            'ld_offset_loc': [150, 60],
            'ld_offset_scale': [1, 1],
            'scale_ss': [1, 1],  # assumed big pics
            'rad_rot': random.uniform(-0.1, -0.2),
            'alpha_y_range': [0.01, 0.3],
            'up_down': None,  # key checked for alpha
            'zorder': 200,
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_srs_gi6(_s):
        srs_gi = {
            'id': 6,
            'init_frames': [16, 26, 36, 46, 56],
            'frames_tot': 300,
            'v_linear_loc': [-0.3, 0],
            'v_linear_scale': [0.02, 0.01],
            'ld': _s.ld,  # finish_info
            'ld_offset_loc': [60, 80],
            'ld_offset_scale': [1, 1],
            'scale_ss': [1, 1],  # assumed big pics
            'rad_rot': random.uniform(-0.1, -0.2),
            'alpha_y_range': [0.1, 0.3],
            'up_down': None,  # key checked for alpha
            'zorder': 90,
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_srs_gi7(_s):
        srs_gi = {
            'id': 7,
            'init_frames': [17, 27, 37, 47, 57],
            'frames_tot': 300,
            'v_linear_loc': [-0.3, 0],
            'v_linear_scale': [0.15, 0.02],
            'ld': _s.ld,  # finish_info
            'ld_offset_loc': [80, 90],
            'ld_offset_scale': [1, 1],
            'scale_ss': [1, 1],  # assumed big pics
            'rad_rot': random.uniform(-0.1, -0.3),
            'alpha_y_range': [0.1, 0.3],
            'up_down': None,  # key checked for alpha
            'zorder': 90,
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi

    def gen_srs_gi8(_s):
        srs_gi = {
            'id': 8,
            'init_frames': [18, 28, 38, 48, 58],
            'frames_tot': 300,
            'v_linear_loc': [-0.3, 0],
            'v_linear_scale': [0.15, 0.02],
            'ld': _s.ld,  # finish_info
            'ld_offset_loc': [100, -20],
            'ld_offset_scale': [1, 1],
            'scale_ss': [1, 1],  # assumed big pics
            'rad_rot': random.uniform(-0.1, -0.3),
            'alpha_y_range': [0.1, 0.3],
            'up_down': None,  # key checked for alpha
            'zorder': 90,
        }

        assert (srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)

        return srs_gi






