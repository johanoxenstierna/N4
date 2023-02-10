"""spark"""

from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
import P as P
import numpy as np
from copy import deepcopy
import random
from src.projective_functions import *
from src.gen_trig_fun import gen_alpha

class Sp(AbstractLayer, AbstractSSS):

    def __init__(_s, sh, id_int, f=None):
        AbstractLayer.__init__(_s)

        _s.sh = sh
        _s.id = sh.id + "_f" + "_sp_" + str(id_int)

        if f != None:
            _s.id = sh.id + "_f" + "_sp_" + str(id_int)
            _s.f = f
            _s.gi = deepcopy(f.sps_gi)
            # _s.dyn_gen()  # NO. It's just too many sp
        #     _s.gi['frames_tot'] = 150
        #     assert(_s.gi['frames_tot'] < _s.f.gi['frames_tot'])
        #     _s._flip_it = True
        #     _s.gi['r_f_d_type'] = 'after'  # after is what is kept
        else:
            _s.f = None

            if random.random() < 0.5:  # TODO. should be in gi obviously.
                _s._sps_type = '0'
            else:
                _s._sps_type = '2'

            _s.id = sh.id + "_sp" + _s._sps_type + '_' + str(id_int)

        AbstractSSS.__init__(_s, sh, _s.id)

    def gen_scale_vector(_s):

        scale_ss = []
        return scale_ss

    def dyn_gen(_s, i, gi=None):

        """
        Basically everything moved from init to here.
        This can only be called when init frames are synced between
        """

        if gi == None:  # gi pre-computed
            assert(_s.f != None)
            _s.gi = deepcopy(_s.f.sps_gi)
            # _s.gi['frames_tot'] = 150
            assert (_s.gi['frames_tot'] < _s.f.gi['frames_tot'])  # f have to last longer than sp
            # _s._flip_it = True
            _s.gi['r_f_d_type'] = 'after'  # after is what is kept
            # _s._up_down = 'down'
        else:  # sh sps
            '''Has to be done for REPEATED sp. 
            Problem is that each sh only has a token amount of sps, so if re-generation is sought
            the gi has to be generated dynamically. 
            Use mod here or smthn. 
            Its init_frames start at sh.gi level, i.e. all of them 
            '''
            # if i in _s.sh.gi.sps_gi0['init_frames'] and _s._sps_type == '0':
            _s.gi = gi
            _s.init_frame = _s.set_init_frame(i)

        _s.finish_info()

        '''OBS frames_tot is same as f. But projectile needs to be generated with more frames'''
        if _s.gi['r_f_d_loc'] == 0:
            frames_tot_d = int(_s.gi['frames_tot'])
        else:
            frames_tot_d = int(_s.gi['frames_tot'] * _s.gi['r_f_d'])

        frames_tot_and_d = _s.gi['frames_tot'] + frames_tot_d

        # if _s.f != None:
        _s.xy_t = simple_projectile(v=_s.gi['v'], theta=_s.gi['theta'],
                                    frames_tot=frames_tot_and_d, up_down=_s.gi['up_down'])

        _s.xy = shift_projectile(_s.xy_t, origin=(_s.gi['ld'][0] + _s.gi['ld_offset'][0],
                                                  _s.gi['ld'][1] + _s.gi['ld_offset'][1]),
                                 frames_tot_d=frames_tot_d,
                                 up_down=_s.gi['up_down'],
                                 r_f_d_type=_s.gi['r_f_d_type'])

        # _s.alphas = np.linspace(0.6, 0.0, num=len(_s.xy))

        if _s.f != None:
            _s.alphas = np.linspace(0.6, 0.0, num=_s.gi['frames_tot'])
        else:
            '''CHANGE ALPHA TO NORMAL'''
            _s.alphas = gen_alpha(_s, frames_tot=_s.gi['frames_tot'], y_range=[0, 0.8])

        # _s.alphas = np.sin(list(range(0, int(_s.gi['frames_tot'] / 2 * np.pi))))
        if _s.alphas[0] > 0.3:
            asdf = 5
        assert (len(_s.alphas) == len(_s.xy))
        assert (_s.gi['frames_tot'] == len(_s.alphas))

    def set_init_frame(_s, i):

        # gi = None
        # init_frame = None
        #
        # if _type == 'sh0':
        #     assert(i in _s.sh.gi.sps_init_frames)  # at this point this is the same gi as _s.sh.gi.sps_gi
        #     gi = deepcopy(_s.sh.gi.sps_gi0)  # could take it directly from sh but this is simpler
        #     assert (i in gi['init_frames'])
        #     index_init_frames = gi['init_frames'].index(i)
        #     init_frame = gi['init_frames'][index_init_frames] + random.randint(0, gi['init_frame_max_dist'])
        # elif _type == 'sh2':
        #     # assert(i in _s.gi['init_frames'])
        #     gi = deepcopy(_s.sh.gi.sps_gi2)
        #     assert (i in gi['init_frames'])
        index_init_frames = _s.gi['init_frames'].index(i)
        init_frame = _s.gi['init_frames'][index_init_frames] + random.randint(0, _s.gi['init_frame_max_dist'])

        # _s.gi['r_f_d_type'] = 'after'  # after means what is kept

        return init_frame

    def finish_info(_s):

        """This is written manually and adds/changes things in gi.
        Usually this function is run dynamically depending on coordinates of
        a parent layer at a certain frame. But not always.
        """

        # _s.gi['max_ri'] = np.max(_s.extent[:, 1])
        _s.gi['v'] = max(13, abs(np.random.normal(loc=_s.gi['v_loc'], scale=_s.gi['v_scale'])))
        theta = np.random.normal(loc=_s.gi['theta_loc'], scale=_s.gi['theta_scale'])  # + np.pi / 2
        _s.gi['theta'] = theta
        _s.gi['r_f_d'] = max(0.001, np.random.normal(loc=_s.gi['r_f_d_loc'], scale=_s.gi['r_f_d_scale']))
        _s.gi['ld_offset'] = [np.random.normal(loc=_s.gi['ld_offset_loc'][0], scale=_s.gi['ld_offset_scale'][0]),
                              np.random.normal(loc=_s.gi['ld_offset_loc'][1], scale=_s.gi['ld_offset_scale'][1])]

        '''Colors'''
        R_start = min(1, np.random.normal(loc=_s.gi['R_ss'][0], scale=_s.gi['R_scale']))
        G_start = min(1, np.random.normal(loc=_s.gi['G_ss'][0], scale=_s.gi['G_scale']))
        B_start = min(1, np.random.normal(loc=_s.gi['B_ss'][0], scale=_s.gi['B_scale']))

        R_start = max(0.01, R_start)
        G_start = max(0.01, G_start)
        B_start = max(0.01, B_start)

        _s.R = np.linspace(R_start, _s.gi['R_ss'][1], num=_s.gi['frames_tot'] + 5)
        _s.G = np.linspace(G_start, _s.gi['G_ss'][1], num=_s.gi['frames_tot'] + 5)
        _s.B = np.linspace(B_start, _s.gi['B_ss'][1], num=_s.gi['frames_tot'] + 5)

        try:
            assert(min(_s.R) > 0)
            assert(min(_s.G) > 0)
            assert(min(_s.B) > 0)
        except:
            raise Exception("R G B not within range")

        _s.gi['zorder'] = random.randint(_s.sh.gi.zorder - 3, _s.sh.gi.zorder + 16)

        # OBS NEW FROM SR SUPER IMPORTANT:
        if _s.id[0] == '3':
            c_id = _s.gi['c_id']
            if c_id not in _s.sh.cs.keys():
                raise Exception("trying to dyn_gen an sp which is tied to a c that does not exist. "
                                "Check info file to see if c_id is set correctly. No pic to check for sp.")

            '''This could be written to gi of sr'''
            _s.gi['ld'] = [_s.sh.cs[c_id].extent[-3, 0], _s.sh.cs[c_id].extent[-3, 2]]

