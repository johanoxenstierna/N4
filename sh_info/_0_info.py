
from sh_info.shInfoAbstract import ShInfoAbstract
import P as P

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
        _s.ld_ss = [[100, 120], [100, 120]]
        _s.fs_gi = _s.gen_fs_gi()
        _s.zorder = 5

    def gen_fs_gi(_s):
        """
        This has to be provided because the fs are generated w.r.t. sh.
        This is like the constructor input for F class
        """

        fs_gi = {}
        # fs_gi['init_frames'] = [3, 20, 50, 100, 120, 150, 160, 200]
        fs_gi['init_frames'] = [3]
        fs_gi['ld_offset_ss'] = [[30, -15], [10, -15]]
        fs_gi['ld_offset_rand_ss'] = [[10, 5], [5, 5]]
        fs_gi['scale_ss'] = [0, 1.0]
        fs_gi['frame_ss'] = _s.frame_ss  # simpler with this
        fs_gi['frames_tot'] = _s.frames_tot
        fs_gi['ld_ss'] = _s.ld_ss
        fs_gi['fs_hardcoded'] = {}  # {id: {}}
        fs_gi['zorder'] = 5

        # fs_gi['sp'] = {'v': 20, 'theta': 360}
        fs_gi['sp'] = {}

        return fs_gi




