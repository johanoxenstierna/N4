
MAP_SIZE = 's0'  # 214, 181
# MAP_SIZE = 'small'  # 488, 185
# MAP_SIZE = 'big'  # 1280 720  # also check ship info (copy-paste)
FRAMES_START = 0
FRAMES_STOP = None  # frames info: 1200/min 12000 for 10 min.   Takes ~30 min to gen 1000 frames  7200
if MAP_SIZE == 's0':
    FRAMES_START = 0
    FRAMES_STOP = 500
FRAMES_TOT = FRAMES_STOP - FRAMES_START

# A (what to animate) ========
A_AFFINE_TRANSFORM = 0  # compulsary probably at least for ships
A_SAILS = 0
A_SAIL_HEIGHTS_TROUGHS_TRANSFORM = 0
A_SR = 1  # smokr
A_WAVES = 0
A_FIRE = 1  # use set extent
A_SP = 1  # sparks
A_EXPLS = 0
A_FIRING_BRIGHTNESS = 0  # does not requires EXPLS (for now!)
A_SPLS = 0
A_STATIC_ALPHA_DARKENING = 0  # A_HSV_TRANSFORM = 1  # REMOVED  replaced with this

PR_MOVE_BLACK = 0  # what to pre-compute (doesn't affect rendering time that much)
PR_ZIGZAG = 0

GLOBAL_ALPHA_DARKENING = [[]]  # TODO: THIS USED BY SMOKRS ETC.
NUM_WAVES = 8  # NUM per pic!!!
NUM_SMOKAS = 7  # CHECK THAT THESE ARE INITED SEQUENTIALLY (to avoid same smoka repeating)
NUM_SMOKRS = 5
NUM_EXPLS = 1  # capability for >1 there but might not be needed
NUM_SPLS = 3  # capability for >1 there but might not be needed

WAVES_STEPS_P_CYCLE = 90  #
SAIL_STEPS_P_CYCLE = 360  # 120 # (6 sec)
SAIL_CYCLES = 3
WS_STEPS = 40  # 2s  wave front of ship
# SPLASH_STEPS_P_CYCLE = 150
# SPL_FRAME_OFFSET = 25  # not good design-wise
EXPL_CYCLES = 8  # how often broadsides happen (HAS TO BE MOVED INTO SHIP INFO)

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