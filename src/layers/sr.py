


import numpy as np
from copy import deepcopy
import random

import P as P
from src.gen_extent_triangles import *
from src.layers.abstract import AbstractLayer, AbstractSSS
from src.gen_trig_fun import gen_alpha, gen_scale_lds
from src.projective_functions import *

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

        if sh.id == '1':
            _s.dyn_gen(gi=sh.gi.srs_gi['0'])  # creates REPEATED srs. C-tied sr are dyn_gened in main

    def dyn_gen(_s, i=None, gi=None):

        if gi != None:
            _s.gi = gi
        else:
            pass  # gi already created

        if i != None:  # only used by the non-repeatables
            _s.init_frame = _s.set_init_frame(i)

        _s.finish_info()

        frames_to_d = int(_s.gi['frames_tot'] * _s.gi['r_f_d'])
        frames_tot_and_d = _s.gi['frames_tot'] + frames_to_d

        if _s.gi['v'] > 20:
            adf = 5

        _s.xy_t = simple_projectile(v=_s.gi['v'], theta=_s.gi['theta'],
                                    frames_tot=frames_tot_and_d, rc=1, up_down=_s.gi['up_down'])

        origin_ = (_s.gi['ld'][0] + _s.gi['ld_offset'][0], _s.gi['ld'][1] + _s.gi['ld_offset'][1])
        _s.xy = shift_projectile(_s.xy_t, origin=origin_, up_down=_s.gi['up_down'], frames_tot_d=frames_to_d,
                                 r_f_d_type='after')

        # _s.extent, _s.extent_t, lds_vec, _s.scale_vector = gen_extent(_s.gi, pic=_s.pic)
        # fun_plot = 'sr'  # smokr but fun plot is same

        # _s.scale_vector = gen_scale_lds(_s.gi['frames_tot'], fun_plot='sr')
        _s.scale_vector = np.linspace(0.001, 1, num=_s.gi['frames_tot'])
        if _s.id[0] == '3':  # OBS CAN MAKE IT APPEAR AS IF THETA IS WRONG
            _s.scale_vector = np.linspace(0.2, 1, num=_s.gi['frames_tot'])

        _s.rotation = np.linspace(0.01, 1, num=len(_s.scale_vector))

        _s.alpha = gen_alpha(_s, frames_tot=_s.gi['frames_tot'])

    def set_init_frame(_s, i):

        index_init_frames = _s.gi['init_frames'].index(i)
        init_frame = _s.gi['init_frames'][index_init_frames] #  add rand earlier + random.randint(0, _s.gi['init_frame_max_dist'])

        return init_frame

    def finish_info(_s):
        """This is written manually and adds/changes things in gi.
        Usually this function is run dynamically depending on coordinates of
        a parent layer at a certain frame. But not always.
        """

        _s.gi['v'] = np.random.normal(loc=_s.gi['v_loc'], scale=_s.gi['v_scale'])
        theta = _s.gi['theta_loc']  # np.pi / 2 + np.random.normal(loc=_s.gi['theta_loc'], scale=_s.gi['theta_scale'])
        _s.gi['theta'] = theta
        _s.gi['r_f_d'] = np.random.normal(loc=_s.gi['r_f_d_loc'], scale=_s.gi['r_f_d_scale'])
        _s.gi['ld_offset'] = [np.random.normal(loc=_s.gi['ld_offset_loc'][0], scale=_s.gi['ld_offset_scale'][0]),
                              np.random.normal(loc=_s.gi['ld_offset_loc'][1], scale=_s.gi['ld_offset_scale'][1])]

        # OBS SUPER IMPORTANT:
        if _s.id[0] == '3':
            c_id = _s.gi['c_id']
            if c_id not in _s.sh.cs.keys():
                raise Exception("trying to dyn_gen an sr which is tied to a c that does not exist. "
                                "c_id: " + c_id + " sr_id: " + _s.id + ". Check that pic is in there.")

            '''This could be written to gi of sr'''
            _s.gi['ld'] = [_s.sh.cs[c_id].extent[-3, 0], _s.sh.cs[c_id].extent[-3, 2]]

        # if _s.id[0] == '3':
        # if _s.id[0:6] == '3_sr_0':
        #

    # def gen_sps_gi(_s):  # PENDING DEL
    #     """
    #     THESE ARE AVERAGES
    #     r_f_s gives ratio of frames that should be discarded, i.e. the ratio that the sp should
    #     climb up the projectile (before shifting)
    #     """
    #     sps_gi = {'v_loc': 12, 'v_scale': 10,
    #               'theta_loc': -0.2, 'theta_scale': 0.08,
    #               'r_f_d_loc': 0.4, 'r_f_d_scale': 0.05,
    #               'origin': (120, 50),
    #               'offset_x_loc': 0, 'offset_x_scale': 0.03,
    #               'offset_y_loc': 0, 'offset_y_scale': 0.02}
    #     return sps_gi