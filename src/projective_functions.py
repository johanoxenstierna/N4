import copy

import numpy as np


def simple_projectile(v, theta, frames_tot):
    """
    OBS this is for midpoint, i.e. SINGLE PIXEL
    See tutorial for using a patch to make it larger than single pixel
    always assumes origin is at 0, 0, so needs shifting afterwards.
    """

    xy = np.zeros((frames_tot, 2))  # MIDPOINT

    G = 9.8
    # t_flight = 2 * v * np.sin(theta) / G
    # t = np.linspace(0, t_flight, num_frames)
    # x = v * np.cos(theta) * t
    # y = v * np.sin(theta) * t - 0.5 * G * t ** 2

    t_flight = 2 * v * np.sin(theta) / G
    t = np.linspace(0, t_flight, frames_tot)
    x = v * np.cos(theta) * t
    y = v * np.sin(theta) * t - 0.5 * G * t ** 2

    xy[:, 0] = x
    xy[:, 1] = y

    return xy


def shift_projectile(xy_t, origin=None, frames_to_discard=None):
    """shifts it to desired xy
    y is flipped because 0 y is at top"""

    xy = copy.deepcopy(xy_t)

    '''
    y0: First it needs to be flipped bcs all values are pos to start with, but it needs to be neg.  
    '''
    xy[:, 1] *= -1  # flip it. Now all neg

    '''Shift start y to upper portion of curve. 
    Find delta to t origin
    OBS OBS OBS: This is currently only set up for right motion'''

    xy = xy[frames_to_discard:, :]
    x_shift_r_f_d = xy[0, 0]  # TODO: change for left motion
    y_shift_r_f_d = xy[0, 1]

    '''x'''
    xy[:, 0] += origin[0] - x_shift_r_f_d  # x

    '''
    y1: Move. y_shift_r_f_d is MORE shifting downward (i.e. positive), but only the latter portion 
    of frames is shown.
    '''
    xy[:, 1] += origin[1] - y_shift_r_f_d

    return xy

