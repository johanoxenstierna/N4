
from sh_info.shInfoAbstract import ShInfoAbstract
import P as P
import random

class Sh_0_info(ShInfoAbstract):
    """
    Basically this is the json replacement (also chronicle to some extent).
    Just very basic stuff
    """

    def __init__(_s):
        super().__init__()
        _s.id = '0'
        _s.extent = "static"
        _s.frame_ss = [0, P.FRAMES_STOP - 50]
        _s.frames_tot = _s.frame_ss[1] - _s.frame_ss[0]
        # _s.ld_ss = [[100, 120], [100, 120]]
        _s.ld_ss = [[120, 50], [120, 50]]
        _s.fs_gi = _s.gen_fs_gi()  # OBS: sp_gi generated in f class. There is no info class for f.
        _s.zorder = 5

    def gen_fs_gi(_s):
        """
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        """

        fs_gi = {}
        # fs_gi['init_frames'] = [3, 20, 50, 100, 120, 150, 160, 200]
        init_frames = random.sample(range(1, 200), 10)  # 1-50 is range, 7 is num  + sort
        init_frames.sort()
        fs_gi['init_frames'] = init_frames
        # fs_gi['frames_tot'] = random.randint(170, 220)
        fs_gi['frames_tot'] = random.randint(50, 51)
        fs_gi['ld_offset_ss'] = [[30, -15], [10, -15]]
        fs_gi['ld_offset_rand_ss'] = [[10, 5], [5, 5]]
        # fs_gi['scale_ss'] = [0, 12.0]
        fs_gi['frame_ss'] = _s.frame_ss  # simpler with this
        fs_gi['ld_ss'] = _s.ld_ss
        # fs_gi['ld_ss_offset'] = [[200, 200], [200, 200]]
        fs_gi['ld_ss_offset'] = [[100, 100], [200, 200]]
        fs_gi['fs_hardcoded'] = {}  # {id: {}}
        fs_gi['zorder'] = 5

        return fs_gi





