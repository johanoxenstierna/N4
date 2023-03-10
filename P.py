DEBUG = 0  # if 1 then faster speed on objectsh
MAP_SIZE = 's0'  # 214, 181
MAP_DIMS = (465, 270)  #(233, 141)small  # NEEDED FOR ASSERTIONS

FRAMES_START = 0
FRAMES_STOP = None  # frames info: 1200/min 12000 for 10 min.   Takes ~30 min to gen 1000 frames  7200
if MAP_SIZE == 's0':
    FRAMES_START = 0
    FRAMES_STOP = 1200
FRAMES_TOT = FRAMES_STOP - FRAMES_START

# A (what to animate) ========
A_SRS = 1  # smokr
A_SPS = 1  # sparks  MUST BE 1 (being fixed though)
A_FS = 1  # fires. ALWAYS HAVE SP CHILDREN (IF A_SPS)
A_RS = 1  # rocks
A_LS = 1  # lava
A_CS = 1
A_LIS = 1

NUM_SPS_SH = None  #a
NUM_SPS_F = 50  # used by 0, 5
NUM_SPS_L_TOT = 400  # used by 2, 4   PER PIC!!!
# NUM_SPS_PER_INIT = 50
NUM_SPS_PER_L = 150  # FOR EACH INIT_FRAME
NUM_SPS_C_TOT = 220  # used by 3: Num sp at 1 init frame!
NUM_SPS_PER_C = 30  # used by 3: Num sp at 1 init frame!
NUM_SPS_7_TOT = 400
NUM_SPS_PER_7 = 50

NUM_SRS_SH = 150  # the upper ones. used by 0, 1, 2, 5. THIS IS ONLY USED TO GENERATE COPIES OF PICTURES (HOW MANY SHOULD BE AVAILABLE FOR GIVEN INIT_FRAMES)
NUM_SRS_C = 100  # used by 3. OBS OBS PER PIC, NOT PER C. SRS pics are used by all c
NUM_FS = 20  # the ones that fill init_frames
NUM_RS = 50  # upper bound

SHS_TO_SHOW = ['0', '1', '2', '3', '5', '6', '7']  # , '6', '7']#, '1'] #, '2', '3']
# SHS_TO_SHOW = ['0', '1', '3', '5', '6']  # , '6', '7']#, '1'] #, '2', '3']
# SHS_TO_SHOW = ['6', '2', '3']  # , '6', '7']#, '1'] #, '2', '3']
# SHS_TO_SHOW = ['7', '0']  # , '6', '7']#, '1'] #, '2', '3']
# SHS_TO_SHOW = ['6']  # , '6', '7']#, '1'] #, '2', '3']


