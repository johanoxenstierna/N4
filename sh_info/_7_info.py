
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
        _s.child_names = ['ls', 'srs']
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.init_frames = pulse
        _s.ld = top_point

        _s.ls_gi = _s.gen_ls_gi(pulse)  # NO DYN_GEN
        _s.srs_gi = {'0': _s.gen_srs_gi(pulse)}
        _s.srs_gi_init_frames = _s.srs_gi['0']['init_frames']
        _s.zorder = 110

    def gen_ls_gi(_s, pulse):
        """
        SHARED FOR THE SAME SH. Kind of... makes sense. ld is used for extent, but they are modified
        for each l in l class finish info.
        """

        # lif0, lif1 = _s.distribute_pulse_for_ls(pulse)  # l_init_frame
        lif0 = [pulse[0]]
        lif1 = [pulse[1]]  # OBS REMEMBER l_init_frames below
        # lif2 = [pulse[2]]
        # lif3 = [pulse[3]]
        l_init_frames = lif0 + lif1 #+ lif2 + lif3

        ls_gi = {
            'init_frames_all': l_init_frames,
            'lif0': lif0,
            'lif1': lif1,
            # 'lif2': lif2,
            # 'lif3': lif3,
            'frames_tot0': 100,
            'frames_tot1': 100,
            # 'frames_tot2': 500,
            # 'frames_tot3': 500,
            'ld': _s.ld,
            'ld0': [_s.ld[0] + 22, _s.ld[1] + 158],
            'ld1': [_s.ld[0] + 89, _s.ld[1] + 152],
            'frame_ss': _s.frame_ss,
            'zorder': 120  # 3 is 110
        }

        return ls_gi

    def gen_srs_gi(_s, pulse_srs):
        """
        Tied to ls!
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        """

        srs_gi = {
            'init_frames': copy.deepcopy(pulse_srs),
            'frames_tot': 300,
            'ld': None,  # finish_info
            'ld_offset_loc': [0, 0],
            'ld_offset_scale': [0, 0],
            'scale_ss': [0.01, 2],
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





