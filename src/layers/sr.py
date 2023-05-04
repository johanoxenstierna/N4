


import numpy as np
from copy import deepcopy
import random

import P as P
from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
from src.gen_trig_fun import gen_alpha #gen_scale_lds
from src.trig_functions import _normal, min_max_normalization
from src.projectile_functions import *

class Sr(AbstractLayer, AbstractSSS):

    def __init__(_s, id, pic, sh, num_sr):
        AbstractLayer.__init__(_s)
        _s.id = id  # OBS SRS SHARED BETWEEN C
        _s.sh = sh
        _s.pic = pic  # NOT SCALED

        # _s.gi = deepcopy(sh.gi.srs_gi['0'])

        # PROBLEM: DONT KNOW WHICH GI TO LOAD.
        # if id[0] == '3':  # loads one of several gis
        #     _s.gi = _s.load_gi(id, sh)

        if random.random() < 0.5:  # TODO. should be in gi obviously.
            _s._srs_type = '0'
        else:
            _s._srs_type = '2'

        # _s.id = sh.id + "_sp" + _s._srs_type + '_' + str(id_int)

        AbstractSSS.__init__(_s, sh, id)

        id_s = id.split('_')

        if sh.id in ['0', '1', '5', '6', '5', '7']:
            '''All special inits are done in finish_info'''
            _s.dyn_gen(gi=sh.gi.srs_gi['0'])
        elif sh.id in ['2', '4']:  # sr tied to l

            gi = random.choice(list(sh.gi.srs_gi.values()))

            _s.dyn_gen(gi=gi)

        elif sh.id in ['8']:
            '''NO DYN GEN. Special case. xy done in gi. Its linear motion. '''
            # if id_s[2] == '4':
            _s.gi = deepcopy(sh.gi.srs_gi[id_s[2]])  # tied to pic

            '''This should be generic though:'''
            ld_offset = [np.random.normal(loc=_s.gi['ld_offset_loc'][0], scale=_s.gi['ld_offset_scale'][0]),
                         np.random.normal(loc=_s.gi['ld_offset_loc'][1], scale=_s.gi['ld_offset_scale'][1])]

            _s.gi['ld'] = [_s.gi['ld'][0] + ld_offset[0], _s.gi['ld'][1] + ld_offset[1]]

            _s.gi['v_linear'] = [np.random.normal(loc=_s.gi['v_linear_loc'][0], scale=_s.gi['v_linear_scale'][0]),
                                 np.random.normal(loc=_s.gi['v_linear_loc'][1], scale=_s.gi['v_linear_scale'][1])]

            _s.xy = gen_xy_linear(_s.gi)
            # _s.scale_vector = np.ones(shape=(_s.gi['frames_tot'],))
            # X = np.array(shape=(len(_s.xy,)))  # zeros causes warning
            X = np.arange(0, len(_s.xy))
            sv0 = _normal(X=X, mean=len(X) // 2, var=len(X) // 4, y_range=[0.01, 1])
            # sv1 = np.ones(shape=(len(_s.xy,)))
            # sv = 0.1 * sv0 + 0.9 * sv1
            _s.scale_vector = min_max_normalization(sv0, y_range=[0.5, 0.6])

            _s.rotation_v = np.zeros(shape=(_s.gi['frames_tot'],))
            _s.alpha = gen_alpha(_s, frames_tot=_s.gi['frames_tot'], y_range=_s.gi['alpha_y_range'])


        elif sh.id in ['9']:

            gi = deepcopy(random.choice(list(sh.gi.srs_gi.values())))
            # gi = deepcopy(sh.gi.srs_gi['0'])

            '''Special falling motion. '''
            ld_offset = [np.random.normal(loc=gi['ld_offset_loc'][0], scale=gi['ld_offset_scale'][0]),
                         np.random.normal(loc=gi['ld_offset_loc'][1], scale=gi['ld_offset_scale'][1])]

            gi['ld'] = [gi['ld'][0] + ld_offset[0], gi['ld'][1] + ld_offset[1]]
            _s.xy_t = falling_projectile(gi=gi)
            origin_ = (gi['ld'][0], gi['ld'][1])
            _s.xy = shift_projectile(_s.xy_t, origin=origin_, up_down=gi['up_down'], frames_tot_d=0,
                                     r_f_d_type='after')

            # X = np.arange(0, len(_s.xy))
            # sv0 = _normal(X=X, mean=len(X) // 2, var=len(X) // 4, y_range=[0.01, 1])
            # _s.scale_vector = min_max_normalization(sv0, y_range=[0.5, 0.6])

            _s.scale_vector = np.linspace(gi['scale_ss'][0], gi['scale_ss'][1], num=len(_s.xy))
            gi['rad_rot'] = np.random.normal(loc=gi['rad_rot_loc'], scale=gi['rad_rot_scale'])
            if gi['rad_rot'] > 0 and gi['rad_rot_loc'] < 0:
                gi['rad_rot'] = -gi['rad_rot']
            if gi['rad_rot'] < 0 and gi['rad_rot_loc'] > 0:
                gi['rad_rot'] = -gi['rad_rot']

            _s.rotation_v = np.linspace(0.00, gi['rad_rot'], num=gi['frames_tot'])
            _s.gi = gi  # Uhhh. depcopy needed
            _s.alpha = gen_alpha(_s, frames_tot=gi['frames_tot'], y_range=gi['alpha_y_range'])

            _s.gi['zorder'] = int(np.random.normal(loc=_s.gi['zorder_loc'], scale=_s.gi['zorder_scale']))

    def dyn_gen(_s, i=None, gi=None):

        if gi != None:
            _s.gi = gi
        else:
            pass  # gi already created

        if i != None:  # only used by the non-repeatables
            _s.init_frame = _s.set_init_frame(i)

        _s.finish_info()

        '''OBS THIS PROBABLY ONLY WORKS WITH AFTER'''
        before_after = 'after'
        frames_to_d = int(_s.gi['frames_tot'] * _s.gi['r_f_d'])
        frames_tot_and_d = _s.gi['frames_tot'] + frames_to_d

        if _s.sh.id == '6':
            before_after = 'before'
            frames_to_d = _s.gi['frames_tot']  # JUST GENS EVERYTHING
            frames_tot_and_d = int(_s.gi['frames_tot'] + _s.gi['frames_tot'] - frames_to_d)

        _s.xy_t = simple_projectile(v=_s.gi['v'], theta=_s.gi['theta'],
                                    frames_tot=frames_tot_and_d, rc=1, up_down=_s.gi['up_down'])

        origin_ = (_s.gi['ld'][0] + _s.gi['ld_offset'][0], _s.gi['ld'][1] + _s.gi['ld_offset'][1])
        _s.xy = shift_projectile(_s.xy_t, origin=origin_, up_down=_s.gi['up_down'], frames_tot_d=frames_to_d,
                                 r_f_d_type=before_after)

        # _s.extent, _s.extent_t, lds_vec, _s.scale_vector = gen_extent(_s.gi, pic=_s.pic)
        # fun_plot = 'sr'  # smokr but fun plot is same

        # _s.scale_vector = gen_scale_lds(_s.gi['frames_tot'], fun_plot='sr')
        _s.scale_vector = np.linspace(_s.gi['scale_ss'][0], _s.gi['scale_ss'][1], num=_s.gi['frames_tot'])
        if _s.id[0] == '3':  # OBS CAN MAKE IT APPEAR AS IF THETA IS WRONG
            _s.scale_vector = np.linspace(0.2, _s.gi['scale_ss'][1], num=_s.gi['frames_tot'])

        _s.rotation_v = np.linspace(0.01, abs(_s.gi['rad_rot']), num=len(_s.scale_vector))

        _s.alpha = gen_alpha(_s, frames_tot=_s.gi['frames_tot'], y_range=_s.gi['alpha_y_range'])

        # zorder set from gi in abstract class

    def set_init_frame(_s, i):

        index_init_frames = _s.gi['init_frames'].index(i)
        init_frame = _s.gi['init_frames'][index_init_frames] #  add rand earlier + random.randint(0, _s.gi['init_frame_max_dist'])

        return init_frame

    def finish_info(_s):
        """This is written manually and adds/changes things in gi.
        Usually this function is run dynamically depending on coordinates of
        a parent layer at a certain frame. But not always.
        """

        # assert(_s.id != 8)

        _s.gi['v'] = np.random.normal(loc=_s.gi['v_loc'], scale=_s.gi['v_scale'])
        # theta = _s.gi['theta_loc']  # np.pi / 2 + np.random.normal(loc=_s.gi['theta_loc'], scale=_s.gi['theta_scale'])
        _s.gi['theta'] = np.random.normal(loc=_s.gi['theta_loc'], scale=_s.gi['theta_scale'])
        if _s.id[0] == '0':
            if _s.gi['theta'] < -1.6:
                _s.gi['theta'] = np.random.uniform(-1.6, -1.0)
        _s.gi['r_f_d'] = max(0.01, np.random.normal(loc=_s.gi['r_f_d_loc'], scale=_s.gi['r_f_d_scale']))
        _s.gi['ld_offset'] = [np.random.normal(loc=_s.gi['ld_offset_loc'][0], scale=_s.gi['ld_offset_scale'][0]),
                              np.random.normal(loc=_s.gi['ld_offset_loc'][1], scale=_s.gi['ld_offset_scale'][1])]

        _s.gi['rad_rot'] = np.random.normal(loc=_s.gi['rad_rot_loc'], scale=_s.gi['rad_rot_scale'])
        if _s.gi['rad_rot'] > 0 and _s.gi['rad_rot_loc'] < 0:
            _s.gi['rad_rot'] = -_s.gi['rad_rot']
        if _s.gi['rad_rot'] < 0 and _s.gi['rad_rot_loc'] > 0:
            _s.gi['rad_rot'] = -_s.gi['rad_rot']

        if _s.id[0] == '3':
            c_id = _s.gi['c_id']  # DIRECT MATCHING!
            if c_id not in _s.sh.cs.keys():
                raise Exception("trying to dyn_gen an sr which is tied to a c that does not exist. "
                                "c_id: " + c_id + " sr_id: " + _s.id + ". Check that pic is in there.")

            '''This could be written to gi of sr, but that would require that xy is gened for c first'''
            _s.gi['ld'] = [_s.sh.cs[c_id].extent[-3, 0] - 10, _s.sh.cs[c_id].extent[-3, 2]]

        elif _s.id[0] in ['7']: #same as for 1 instead
            # gi = deepcopy(sh.gi.srs_gi['0'])
            l = random.choice(_s.sh.ls)
            _s.gi['ld'] = l.gi['ld']
            _s.gi['ld_offset'] = [np.random.normal(loc=_s.gi['ld_offset_loc'][0], scale=_s.gi['ld_offset_scale'][0]),
                               np.random.normal(loc=_s.gi['ld_offset_loc'][1], scale=_s.gi['ld_offset_scale'][1])]

        if _s.id[0] in ['0', '1', '4']:
            _s.gi['zorder'] = random.randint(_s.sh.gi.zorder - 3, _s.sh.gi.zorder + 5)
        elif _s.id[0] in ['5']:  #
            # _s.gi['zorder'] = random.randint(_s.sh.gi.zorder + 0, _s.sh.gi.zorder + 10)  # OLD. PERHAPS ONLY SPSHOULD BE DYN
            _s.gi['zorder'] = random.randint(_s.sh.gi.zorder - 0, _s.sh.gi.zorder + 8)


