DEBUG = 0  # if 1 then faster speed on objectsh
MAP_SIZE = 's0'  # 214, 181
MAP_DIMS = (233, 141)  # NEEDED FOR ASSERTIONS

FRAMES_START = 0
FRAMES_STOP = None  # frames info: 1200/min 12000 for 10 min.   Takes ~30 min to gen 1000 frames  7200
if MAP_SIZE == 's0':
    FRAMES_START = 0
    FRAMES_STOP = 700
FRAMES_TOT = FRAMES_STOP - FRAMES_START

# A (what to animate) ========
A_AFFINE_TRANSFORM = 0  # compulsary probably at least for sh
A_SRS = 1  # smokr
A_SPS = 1  # sparks  MUST BE 1 (being fixed though)
A_FS = 1  # fires
A_RS = 1  # rocks
A_LS = 1  # lava
A_CS = 1

PR_MOVE_BLACK = 0  # what to pre-compute (doesn't affect rendering time that much)
PR_ZIGZAG = 0

NUM_SPS_SH = 150  # per sh. used by 1, 2
NUM_SPS_F = 20  # used by 0
NUM_SPS_C = 100  # used by 3: Num sp at 1 init frame!

NUM_SRS_SH = 100  # the upper ones. used by 1
NUM_SRS_C = 100  # OBS OBS PER PIC, NOT PER C. SRS pics are used by all c
NUM_FS = 20
NUM_RS = 20  # upper bound
# NUM_LS = 20

WAVES_STEPS_P_CYCLE = 90  #
SAIL_STEPS_P_CYCLE = 360  # 120 # (6 sec)
SAIL_CYCLES = 3
WS_STEPS = 40  # 2s  wave front of sh

# SHS_TO_SHOW = ['0', '1', '2', '3']  # , '6', '7']#, '1'] #, '2', '3']
# SHS_TO_SHOW = ['1', '0']  # , '6', '7']#, '1'] #, '2', '3']
SHS_TO_SHOW = ['0']  # , '6', '7']#, '1'] #, '2', '3']
