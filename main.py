"""
Sh are needed because it might be useful to
have different settings for different fs

"""

import numpy as np
import random
random.seed(7)  # ONLY HERE
np.random.seed(7)  # ONLY HERE
import time
import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2

from src import gen_layers
from src.ani_helpers import *
import P as P
from src.chronicler import Chronicler

WRITE = 0  #FIX: smoka frames, waves  # change IMMEDIATELY back to zero (it immediately kills old file when re-run)
FPS = 20

Chronicler() # just outputs the json below. MAY BE REMOVED.
with open('./src/chronicle.json', 'r') as f:
    ch = json.load(f)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=FPS, metadata=dict(artist='Me'), bitrate=1200)

fig, ax0 = plt.subplots(figsize=(10, 6))   # pic  214 181

im_ax = []
g = gen_layers.GenLayers(ch)
g.gen_backgr(ax0, im_ax)

shs = g.gen_shs(ax0, im_ax)

if P.A_FIRE:
    shs = g.gen_fs(ax0, im_ax, shs)

# if P.A_SR:
#     shs = g.gen_sr(ax0, im_ax, shs)



'''VIEWER ==========================================='''

brkpoint = 4


def init():
    return im_ax


def animate(i):
    prints = "i: " + str(i) + "  len_im_ax: " + str(len(im_ax))
    for sh_id, sh in shs.items():

        if P.A_FIRE:
            if i in sh.sh_gi.fs_gi['init_frames']:
                f = sh.find_free_obj(type='f')
                if f != None and f.id not in f.gi['fs_hardcoded']:
                    exceeds_frame_max, how_many = f.check_frame_max(i, f.gi['frames_tot'])
                    if exceeds_frame_max == True:
                        # prints += "  smoka exceeds max"
                        f.frames_tot = how_many
                        # continue
                    f.drawn = 1  # this variable can serve multiple purposes (see below, and in set_clock)
                    sh.f_latest_drawn_id = f.id
                    f.init_child_obj(i, f.gi['frames_tot'], dynamic=False)  # uses AbstractSSS
                    # f.gen_dyn_extent_alpha()

                    if P.A_SP:
                        for sp_key, sp in f.sps.items():

                            # sp.drawn = 1
                            sp.init_child_obj(i, sp.f.gi['frames_tot'], dynamic=False)

                else:
                    # pass
                    prints += "  no free smoka"

            for f_id, f in sh.fs.items():

                if f.drawn != 0:  # the 4 from above is needed only the very first iteration it becomes visible
                    f.set_clock(i)

                    drawBool, index_removed = f.ani_update_step(ax0, im_ax)
                    if drawBool == 0:  # dont draw
                        continue
                    elif drawBool == 1:
                        # warp_affine_and_color(i, ax0, im_ax, f, ch)  # parent obj required for sail
                        # print(im_ax[f.index_im_ax].get_alpha())
                        mpl_affine(i, f, ax0, im_ax)
                        im_ax[f.index_im_ax].set_alpha(f.alpha[f.clock])
                    elif drawBool == 2:  # remove
                        decrement_all_index_im_ax(index_removed, shs)
                        # continue  # CANT continue because sp also has to be removed

                    if P.A_SP:
                        for sp_id, sp in f.sps.items():
                            sp.set_clock(i)
                            drawBool, index_removed = sp.ani_update_step(ax0, im_ax, sp=True)
                            if drawBool == 0:
                                continue
                            elif drawBool == 1:
                                # try:
                                if sp.clock < 4:  # TODO: CHANGE THIS TO EXTERNAL FUNCTION
                                    im_ax[sp.index_im_ax].set_data(sp.xy[:sp.clock, 0], sp.xy[:sp.clock, 1])
                                else:
                                    im_ax[sp.index_im_ax].set_data(sp.xy[sp.clock - 3:sp.clock, 0],
                                                                   sp.xy[sp.clock - 3:sp.clock, 1])

                                im_ax[sp.index_im_ax].set_color((sp.R[sp.clock], sp.G[sp.clock], sp.B[sp.clock]))
                                im_ax[sp.index_im_ax].set_alpha(sp.alphas[sp.clock])
                                #
                                # except:
                                #     adf = 6
                            elif drawBool == 2:
                                decrement_all_index_im_ax(index_removed, shs)
                                continue



        print(prints)
                    # im_ax[f.index_im_ax].set_alpha(f.alpha[f.clock])
                    # im_ax[smoka.index_im_ax].set_zorder(smoka.zorder)  # SET IN ANI_UPDATE_STEP

    return im_ax  # if run live, it runs until window is closed

sec_vid = ((P.FRAMES_STOP - P.FRAMES_START) / FPS)
min_vid = ((P.FRAMES_STOP - P.FRAMES_START) / FPS) / 60
print("len of vid: " + str(sec_vid) + " s" + "    " + str(min_vid) + " min")

start_t = time.time()
ani = animation.FuncAnimation(fig, animate, frames=range(P.FRAMES_START, P.FRAMES_STOP),
                              blit=True, interval=1, init_func=init,
                              repeat=False)  # interval only affects live ani. blitting seems to make it crash

if WRITE == 0:
    # pass
    plt.show()
else:
    ani.save('./vids/vid_' + str(WRITE) + '.mp4', writer=writer)

tot_time = round((time.time() - start_t) / 60, 4)
print("minutes to make animation: " + str(tot_time) + " |  min_gen/min_vid: " + str(tot_time / min_vid))  #
