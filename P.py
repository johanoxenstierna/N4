
MAP_SIZE = 's0'  # 214, 181
# MAP_SIZE = 'small'  # 488, 185
# MAP_SIZE = 'big'  # 1280 720  # also check ship info (copy-paste)
FRAMES_START = 0
FRAMES_STOP = None  # frames info: 1200/min 12000 for 10 min.   Takes ~30 min to gen 1000 frames  7200
if MAP_SIZE == 's0':
    FRAMES_START = 0
    FRAMES_STOP = 400
FRAMES_TOT = FRAMES_STOP - FRAMES_START

# A (what to animate) ========
A_AFFINE_TRANSFORM = 0  # compulsary probably at least for ships
A_SRS = 0  # smokr
A_SPS = 1  # sparks
A_FS = 1  # fires
A_RS = 0  # rocks

PR_MOVE_BLACK = 0  # what to pre-compute (doesn't affect rendering time that much)
PR_ZIGZAG = 0

GLOBAL_ALPHA_DARKENING = [[]]  # TODO: THIS USED BY SMOKRS ETC.
NUM_SPS_SH = 1  # per sh.  NUMBER LAUNCH ON SAME FRAME
NUM_SPS_F = 1  # per f  NUMBER LAUNCH DIFFERERNT FRAMES
NUM_SRS = 20
NUM_FS = 1
NUM_RS = 5

WAVES_STEPS_P_CYCLE = 90  #
SAIL_STEPS_P_CYCLE = 360  # 120 # (6 sec)
SAIL_CYCLES = 3
WS_STEPS = 40  # 2s  wave front of ship
# SPLASH_STEPS_P_CYCLE = 150
# SPL_FRAME_OFFSET = 25  # not good design-wise
EXPL_CYCLES = 8  # how often broadsides happen (HAS TO BE MOVED INTO SHIP INFO)

# SHS_TO_SHOW = ['0', '1', '2']  # , '6', '7']#, '1'] #, '2', '3']
SHS_TO_SHOW = ['0']  # , '6', '7']#, '1'] #, '2', '3']
# SHIPS_TO_SHOW = ['0', '2', '3', '4'] #, '3', '4']
# SHIPS_TO_SHOW = ['0']
SMOKRS_LEFT = ['3']  # this is checked TOGETHER with smokr info in ship_info
SMOKRS_RIGHT = ['2']

# EXPLOSION_WIDTH = 8
# EXPLOSION_HEIGHT = 3


'''
Min to time: 
.5: 600
1: 1200  .5: 1800
2: 2400  .5: 3000
3: 3600  .5: 4200
4: 4800  .5: 5400
5: 6000
6: 7200 
'''