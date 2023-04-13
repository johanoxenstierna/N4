DEBUG = 0  # if 1 then faster speed on objectsh
# MAP_SIZE = 's0'  # 214, 181
# MAP_DIMS = (465, 270)  #(233, 141)small  # NEEDED FOR ASSERTIONS
MAP_DIMS = (1280, 720)  #(233, 141)small  # NEEDED FOR ASSERTIONS

FRAMES_START = 0
FRAMES_STOP = 1500  # frames info: 1200/min 12000 for 10 min.   Takes ~30 min to gen 1000 frames  7200
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
NUM_SPS_F = 100  # used by 0, 5
NUM_SPS_L_TOT = 800  # used by 2, 4   PER PIC!!!
# NUM_SPS_PER_INIT = 50
NUM_SPS_PER_L = 10  # FOR EACH INIT_FRAME
NUM_SPS_C_TOT = 400  # used by 3: Num sp at 1 init frame!
NUM_SPS_PER_C = 25  # used by 3: Num sp at 1 init frame!
NUM_SPS_7_TOT = 400
NUM_SPS_PER_7 = 50

NUM_SRS_SH = 150  # the upper ones. used by 0, 1, 2, 4, 5. THIS IS ONLY USED TO GENERATE COPIES OF PICTURES (HOW MANY SHOULD BE AVAILABLE FOR GIVEN INIT_FRAMES)
# NUM_SRS_7 = 5  # NUMBER OF REPEATS PER PIC.
NUM_SRS_8 = 5  # NUMBER OF REPEATS PER PIC.  HARDCODED
NUM_SRS_C = 100  # used by 3. OBS OBS PER PIC, NOT PER C. SRS pics are used by all c
NUM_FS = 10  # the ones that fill init_frames
NUM_RS = 15  # upper bound

# 5: post expl, 6: expl, 7: sr tied to ls, 8: srs up/home/johan/PycharmProjects/N4/images/processed/3/cs/3_c_8.png

SHS_TO_SHOW = ['0', '1', '2', '3', '4', '5', '6', '7', '8']  # , '6', '7']#, '1'] #, '2', '3']
# SHS_TO_SHOW = ['0', '2', '3', '4']  # , '6', '7']#, '1'] #, '2', '3']
# SHS_TO_SHOW = ['7', '3', '6']  # , '6', '7']#, '1'] #, '2', '3']
# SHS_TO_SHOW = ['3', '2']  # , '6', '7']#, '1'] #, '2', '3']
# SHS_TO_SHOW = ['1']  # , '6', '7']#, '1'] #, '2', '3']


