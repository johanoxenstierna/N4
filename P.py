import P

DEBUG = 0  # if 1 then faster speed on objectsh
# MAP_SIZE = 's0'  # 214, 181
# MAP_DIMS = (465, 270)  #(233, 141)small  # NEEDED FOR ASSERTIONS
MAP_DIMS = (1280, 720)  #(233, 141)small  # NEEDED FOR ASSERTIONS

FRAMES_START = 0
FRAMES_STOP = 3000  # frames info: 1200/min 12000 for 10 min.   Takes ~30 min to gen 1000 frames  7200
# if MAP_SIZE == 's0':
#     FRAMES_START = 0
#     FRAMES_STOP = 1200
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
NUM_SPS_F = 100  # used by 0, 5, 6  can be reduced for big bug
NUM_SPS_L_TOT = 2000  # used by 2, 4   PER PIC!!!
# NUM_SPS_PER_INIT = 50
NUM_SPS_PER_L = 20  # FOR EACH INIT_FRAME. OBS IF TOO MANY THRE WONT BE ENOUGH
NUM_SPS_C_TOT = 400  # used by 3: Num sp at 1 init frame!
NUM_SPS_PER_C = 25  # used by 3: Num sp at 1 init frame!
NUM_SPS_7_TOT = 800
NUM_SPS_PER_7 = 150  # 50

NUM_SRS_1 = 600 * 3  # init frames for 1
NUM_SRS_5 = 400 * 4  # 400 * 3 #   # init frames for 5. ONLY FS is done in genesis. THIS IS TOTAL NUMBER OF INIT FRAMES FOR 5. The more, the more often a single sr gets launched.
NUM_SRS_SH = 200 * 4  # Used by 0, 1, 2, 4, 5, 6. THIS IS ONLY USED TO GENERATE COPIES OF PICTURES (HOW MANY SHOULD BE AVAILABLE FOR GIVEN INIT_FRAMES)
# NUM_SRS_7 = 5  # NUMBER OF REPEATS PER PIC.
NUM_SRS_8 = 5  # NUMBER OF REPEATS PER PIC.  HARDCODED
NUM_SRS_C = 100  # used by 3. OBS OBS PER PIC, NOT PER C. SRS pics are used by all c
NUM_FS = 10  # the ones that fill init_frames. TOT: 1000

NUM_RS_PICS = 150
NUM_RS_0 = 50  # upper bound
NUM_RS_2 = 50

# 5: post expl, 6: expl, 7: sr tied to ls, 8: srs up/home/johan/PycharmProjects/N4/images/processed/3/cs/3_c_8.png

SHS_TO_SHOW = ['0', '1', '2', '3', '4', '5', '6', '7', '8']  # , '6', '7']#, '1'] #, '2', '3']
# SHS_TO_SHOW = ['0', '1', '3', '5', '6', '7']  # , '6', '7']#, '1'] #, '2', '3']
# SHS_TO_SHOW = ['0', '1', '3']  # , '6', '7']#, '1'] #, '2', '3']
# SHS_TO_SHOW = ['6', '5']
# SHS_TO_SHOW = ['6']

# THE BUG: 717
# NOT [6, 5], ['6', '0']  6_f_sp_701


