
import numpy as np


def simple_projectile(v, theta, num_frames):
    """
    OBS this is for midpoint, i.e. SINGLE PIXEL
    See tutorial for using a patch to make it larger than single pixel
    always assumes origin is at 0, 0, so needs shifting afterwards.
    """

    xy = np.zeros((num_frames, 2))  # MIDPOINT

    G = 9.8
    # t_flight = 2 * v * np.sin(theta) / G
    # t = np.linspace(0, t_flight, num_frames)
    # x = v * np.cos(theta) * t
    # y = v * np.sin(theta) * t - 0.5 * G * t ** 2

    t_flight = 2 * v * np.sin(theta) / G
    t = np.linspace(0, t_flight, num_frames)
    x = v * np.cos(theta) * t
    y = v * np.sin(theta) * t - 0.5 * G * t ** 2

    xy[:, 0] = x
    xy[:, 1] = y

    return xy


def shift_projectile(xy_t, target):
    """shifts it to desired xy
    y is flipped because 0 y is at top"""

    xy = xy_t
    xy[:, 0] += target[0]  # x

    '''y fix'''
    xy[:, 1] *= -1
    _a = np.min(xy[:, 1])
    xy[:, 1] -= _a

    xy[:, 1] += target[1] + _a

    return xy

