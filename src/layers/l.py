
from src.layers.abstract import AbstractLayer
import P as P
# from src.gen_colors import gen_colors
# import copy
import numpy as np


class L(AbstractLayer):
    """Only 1 extent, use alpha to make visible at frames of choice"""
    def __init__(_s, id, pic, gi):
        AbstractLayer().__init__()
        _s.id = id
        _s.gi = gi  # IMPORTANT replaces _s.gi = ship_info
        _s.pic = pic  # NOT SCALED
        _s.f_latest_drawn_id = "99_99_99_99"
        _s.zorder = gi.zorder



