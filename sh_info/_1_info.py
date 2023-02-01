
from sh_info.shInfoAbstract import ShInfoAbstract
import P as P
import random
import numpy as np

class Sh_1_info(ShInfoAbstract):
    """
    Basically this is the json replacement (also chronicle to some extent).
    Just very basic stuff
    """

    def __init__(_s, init_frames, top_point):
        super().__init__()
        _s.id = '1'
        _s.extent = "static"
        _s.child_names = ['srs']
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]
        _s.init_frames = init_frames
        # _s.ld = [121, 48]
        _s.ld = [top_point[0] - 5, top_point[1] + 5]
        _s.srs_gi = {'0': _s.gen_srs_gi()}  # OBS: sp_gi generated in f class. There is no info class for f.
        _s.srs_gi_init_frames = init_frames
        # _s.zorder = 5

    def gen_srs_gi(_s):
        """
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        """

        srs_gi = {}
        # srs_gi['init_frames'] = [3, 20, 50, 100, 120, 150, 160, 200]
        # init_frames = random.sample(range(1, 200), 20)  # 1-50 is range, 7 is num  + sort
        # init_frames.sort()

        # srs_gi['init_frames'] = init_frames
        srs_gi['init_frames'] = [x + 30 for x in _s.init_frames]

        # fs_gi['frames_tot'] = random.randint(170, 220)
        srs_gi['frames_tot'] = 200
        assert(srs_gi['init_frames'][-1] + srs_gi['frames_tot'] < P.FRAMES_STOP)
        srs_gi['ld'] = [_s.ld[0] - 0, _s.ld[1]]  # -6 TUNED WITH affine2D.translate!!!
        srs_gi['ld_offset_loc'] = [0, 1]  # OBS there is no ss, only start!
        srs_gi['ld_offset_scale'] = [1, 1]  # OBS there is no ss, only start!
        # srs_gi['ld_offset_rand'] = [10, 5], [5, 5]
        srs_gi['frame_ss'] = _s.frame_ss  # simpler with this
        srs_gi['sr_hardcoded'] = {}
        srs_gi['v_loc'] = 16  # rc=2
        srs_gi['v_scale'] = 4
        srs_gi['theta_loc'] = -0.6 * 2 * np.pi  # radians!
        srs_gi['theta_scale'] = 0.1
        srs_gi['r_f_d_loc'] = 0.05
        srs_gi['r_f_d_scale'] = 0.00
        srs_gi['up_down'] = 'up'
        srs_gi['zorder'] = 1000


        return srs_gi





