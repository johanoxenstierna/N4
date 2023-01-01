import os

import numpy as np

import P as P
from matplotlib.pyplot import imread

def load_pics():
    """LOADS BGR
    ch needed to see if smoka_hardcoded is used """

    pics = {}
    # pics['waves'] = {}
    # pics['spls'] = {}
    pics['sh'] = {}
    # pics['xtra'] = {}
    # pics['smokas'] = {}
    # pics['smokrs'] = {}
    # pics['expls'] = {}
    # pics['specials'] = {}

    if P.MAP_SIZE == 's0':
        # pics['backgr_d'] = imread('./images/processed/navarino_s0d.png')  # 482, 187
        # pics['backgr_d'] = imread('./images/processed/temp.png')  # 482, 187
        pics['backgr_d'] = imread('./images/processed/mdoom3_small.png')  # 482, 187
        aadf = 6
    # else:
    #     pics['backgr'] = imread('./images/raw/backgr.png')  # 482, 187
    #     pics['frame'] = imread('./images/processed/frame.png')  # 482, 187
    #     # pics['frame'] = imread('./images/raw/frame_pic.png')

    # PATH = './images_mut/specials/'
    # _, _, file_names = os.walk(PATH).__next__()
    # for file_name in file_names:
    #     pics['specials'][file_name[:-4]] = imread(PATH + file_name)  # without .png

    # UNIQUE PICTURES FOR A CERTAIN OBJECT (SHIP is the parent structure)
    PATH = './images/processed/'
    _, folder_names0, _ = os.walk(PATH).__next__()
    for folder_name0 in folder_names0:  # shs

        pics['sh'][folder_name0] = {}
        # pics['ships'][folder_name]['sails'] = {}
        # pics['ships'][folder_name]['smokas'] = {}
        # pics['ships'][folder_name]['smokrs'] = {}
        # pics['ships'][folder_name]['expls'] = {}
        # pics['ships'][folder_name]['spls'] = {}
        folder_names1 = ['fs', 'srs', 'rs']
        pics['sh'][folder_name0]['fs'] = {}
        pics['sh'][folder_name0]['srs'] = {}
        pics['sh'][folder_name0]['rs'] = {}
        for folder_name1 in folder_names1:
            try:
                _, _, file_names = os.walk(PATH + '/' + folder_name0 + '/' + folder_name1).__next__()
            except:
                print(folder_name1 + " does not exist for " + folder_name0)
                continue
            for file_name in file_names:
                if folder_name1 == 'fs':
                    pic = imread(PATH + folder_name0 + '/' + folder_name1 + '/' + file_name)  # without .png
                    pic = np.flipud(pic)
                    for i in range(P.NUM_FS):
                        pics['sh'][folder_name0][folder_name1][file_name[:-4] + '_' + str(i)] = pic

                elif folder_name1 == 'srs':
                    pic = imread(PATH + folder_name0 + '/' + folder_name1 + '/' + file_name)  # without .png
                    pic = np.flipud(pic)
                    for i in range(P.NUM_SRS):
                        pics['sh'][folder_name0][folder_name1][file_name[:-4] + '_' + str(i)] = pic
                elif folder_name1 == 'rs':
                    pic = imread(PATH + folder_name0 + '/' + folder_name1 + '/' + file_name)  # without .png
                    pic = np.flipud(pic)
                    for i in range(P.NUM_RS):
                        pics['sh'][folder_name0][folder_name1][file_name[:-4] + '_' + str(i)] = pic
                    pics['sh'][folder_name0][folder_name1][file_name[:-4]] = pic
                else:
                    pic = imread(PATH + folder_name0 + '/' + folder_name1 + '/' + file_name)  # without .png
                    pics['sh'][folder_name0][folder_name1][file_name[:-4]] = pic

                    # elif len(name_split) > 1 and name_split[1] == 's' and P.A_SAILS:
                #     # aa = imread(PATH + '/' + folder_name + '/' + file_name)
                #     pics['sh'][folder_name]['sails'][file_name[:-4]] = imread(PATH + '/' + folder_name + '/' + file_name)
                # elif len(name_split) > 1 and len(name_split) < 4 and name_split[1] == 'a' and P.A_SMOKAS:
                #
                #     # Only 1 copy of hardcoded smokas used
                #     aa = ch['ships'][folder_name]['smokas_hardcoded']['ids']
                #     if file_name[:-4] in ch['ships'][folder_name]['smokas_hardcoded']['ids']:
                #         pics['ships'][folder_name]['smokas'][file_name[:-4]] = \
                #             imread(PATH + '/' + folder_name + '/' + file_name)
                #     else:  # several copies
                #         for i in range(P.NUM_SMOKAS):
                #             # aa = imread(PATH + '/' + folder_name + '/' + file_name)
                #             pics['ships'][folder_name]['smokas'][file_name[:-4] + '_' + str(i)] = \
                #                 imread(PATH + '/' + folder_name + '/' + file_name)

            adf = 5

    return pics


# PATH = './images/processed/waves/'
    # _, _, file_names = os.walk(PATH).__next__()
    # if P.A_WAVES:
    #     for file_name in file_names:
    #         for i in range(P.NUM_WAVES):  # OBS THIS IS NUM OF COPIES PER WAVE, NOT AGGREGATE
    #             # for file_name in file_names:
    #             #     if int(file_name.split('_')[1]) == i:
    #             pics['waves'][file_name[:-4] + '_' + str(i)] = imread(PATH + file_name)  # without .png
    #             # break  # found wave
    #             # if P.MAP_SIZE == 'small' and file_name[5] == 's':
    #             # pics['waves'][file_name[:-4] + '_' + str(i)] = imread(PATH + file_name)  # without .png
    #
    #             # elif P.MAP_SIZE != 'small' and file_name[5] != 's':
    #             #     pics['waves'][file_name[:-4] + '_' + str(i)] = imread(PATH + file_name)  # without .png


    # pics['ships']['ship_3'] = imread('./images_mut/ships/ship_3.png')  # 105, 145
    # pics['ships']['ship_1'] = imread('./images_mut/ships/ship_1.png')  # 105, 145
    # pics['explosions']['explosion_0'] = imread('./images_mut/expls/explosion_0.png')

    # COPIES OF THE SAME EXPLS ARE ADDED TO EACH SHIP
    # PATH = './images/processed/expls/'
    # _, _, file_names = os.walk(PATH).__next__()
    # for file_name in file_names:
    #     pic = imread(PATH + file_name)
    #     for ship_id, ship in pics['ships'].items():
    #         for i in range(P.NUM_EXPLS):
    #             ship['expls'][file_name[:-4] + '_' + str(i)] = pic
    #
    # # COPIES OF THE SAME SPL ARE ADDED TO EACH SHIP
    # PATH = './images/processed/spls/'
    # _, _, file_names = os.walk(PATH).__next__()
    # for file_name in file_names:
    #     pic = imread(PATH + file_name)
    #     for ship_id, ship in pics['ships'].items():
    #         for i in range(P.NUM_SPLS):
    #             ship['spls'][file_name[:-4] + '_' + str(i)] = pic
    #
    # # COPIES OF THE SAME SMOKR ARE ADDED TO EACH SHIP
    # PATH = './images/processed/smokrs/'
    # _, _, file_names = os.walk(PATH).__next__()
    # for file_name in file_names:
    #     pic = imread(PATH + file_name)
    #     for ship_id, ship in pics['ships'].items():
    #         for i in range(P.NUM_SMOKRS):
    #             ship['smokrs'][file_name[:-4] + '_' + str(i)] = pic