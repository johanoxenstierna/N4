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

WRITE = 0  # 5
#FIX: smoka frames, waves  # change IMMEDIATELY back to zero (it immediately kills old file when re-run)
FPS = 20

# Chronicler() # just outputs the json below. MAY BE REMOVED.
# with open('./src/chronicle.json', 'r') as f:
#     ch = json.load(f)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=FPS, metadata=dict(artist='Me'), bitrate=1200)

fig, ax0 = plt.subplots(figsize=(10, 6))   # pic  214 181

im_ax = []
g = gen_layers.GenLayers()
g.gen_backgr(ax0, im_ax)

shs = g.gen_shs(ax0, im_ax)

if P.A_FS:
    shs = g.gen_fs(ax0, im_ax, shs)

if P.A_SPS:
    shs = g.gen_sps(ax0, im_ax, shs)  # OBS children of fs NOT GENERATED HERE

if P.A_SRS:
    shs = g.gen_srs(ax0, im_ax, shs)

if P.A_RS:
    shs = g.gen_rs(ax0, im_ax, shs)

if P.A_LS:
    shs = g.gen_ls(ax0, im_ax, shs)


'''VIEWER ==========================================='''
brkpoint = 4

def init():
    return im_ax


def animate(i):

    prints = "i: " + str(i) + "  len_im_ax: " + str(len(im_ax))
    for sh_id, sh in shs.items():

        if i == 59:
            dadf = 5

        if P.A_FS and 'fs' in sh.gi.child_names:
            if i in sh.gi.fs_gi['init_frames']:
                f = sh.find_free_obj(type='f')
                if f != None and f.id not in f.gi['fs_hardcoded']:
                    prints += "  adding f"
                    exceeds_frame_max, how_many = f.check_frame_max(i, f.gi['frames_tot'])
                    if exceeds_frame_max == True:
                        print("EXCEEDS MAX\n")
                        f.frames_tot = how_many

                    f.drawn = 1  # this variable can serve multiple purposes (see below, and in set_clock)
                    sh.f_latest_drawn_id = f.id
                    f.init_child_obj(i, f.gi['frames_tot'], dynamic=False)  # uses AbstractSSS
                    # f.gen_dyn_extent_alpha()

                    # '''Prob has to be let go'''
                    if P.A_SPS:
                        for sp_key, sp in f.sps.items():
                            # if sp.f is not None:
                            #     if sp.f.id == f.id:
                            assert(sp.f != None)
                            sp.dyn_gen(i)
                            sp.drawn = 1
                            prints += "  adding sp"
                            sp.init_child_obj(i, sp.gi['frames_tot'], dynamic=False)

                        # adf = 5
                else:
                    prints += "  no free f"

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
                        # im_ax[f.index_im_ax].set_alpha(0.01)

                    elif drawBool == 2:  # remove
                        prints += "  removing f"
                        decrement_all_index_im_ax(index_removed, shs)

                        # continue  # CANT continue because sp also has to be removed

                for sp_id, sp in f.sps.items():  # CHILD OF f
                    assert(sp.f != None)
                    if sp.drawn != 0:
                        sp.set_clock(i)
                        drawBoolSP, index_removed = sp.ani_update_step(ax0, im_ax, sp=True)
                        if drawBoolSP == 0:
                            continue
                        elif drawBoolSP == 1:
                            # try:
                            if sp.clock < 4:  # TODO: CHANGE THIS TO EXTERNAL FUNCTION
                                im_ax[sp.index_im_ax].set_data(sp.xy[:sp.clock, 0], sp.xy[:sp.clock, 1])
                            else:
                                try:
                                    im_ax[sp.index_im_ax].set_data(sp.xy[sp.clock - 3:sp.clock, 0],
                                                                   sp.xy[sp.clock - 3:sp.clock, 1])
                                    im_ax[sp.index_im_ax].set_color((sp.R[sp.clock], sp.G[sp.clock], sp.B[sp.clock]))
                                except:
                                    raise Exception("Adf")

                            try:
                                im_ax[sp.index_im_ax].set_alpha(sp.alphas[sp.clock])
                            except:
                                asdf = 5

                            # im_ax[sp.index_im_ax].set_alpha(1)
                            #
                            # except:
                            #     adf = 6
                        elif drawBoolSP == 2:
                            prints += "  removing sp"
                            decrement_all_index_im_ax(index_removed, shs)
                            # continue

        if P.A_SPS and 'sps' in sh.gi.child_names:  # SH sps
            '''NOT f'''
            if i == 20:
                adf = 5
            if i in sh.gi.sps_init_frames:
                '''This sets an init frame for the sp IN THE FUTURE'''

                # HERE EXTEND THIS TO LOOP
                # for _ in range(len(sh.sps)):
                for _ in range(50):
                    sp = sh.find_free_obj(type='sp')

                    '''SINCE OBJECT HASNT BEEN DRAWN YET IT IS
                    STILL FREE. PERHAPS DONT LOOP OVER ALL SPS, 
                    '''
                    if sp != None:
                        assert (sp.f == None)

                        if i in sh.gi.sps_gi0['init_frames']:
                            prints += "  adding sp0"
                            sp.dyn_gen(i, _type='sh0')  # THIS UPDATES gi AND sets init_frame
                        elif i in sh.gi.sps_gi2['init_frames']:
                            prints += "  adding sp2"
                            sp.dyn_gen(i, _type='sh2')
                    else:
                        prints += "  couldnt add sp"

            # HERE FRAME_SS IS THE SAME FOR EVERY SP HERE
            for sp_id, sp in sh.sps.items():

                try:
                    _ = sp.init_frame
                except:
                    sp.init_frame = -999

                if sp.init_frame == i:  # only for sh sp
                    sp.drawn = 1
                    sp.init_child_obj(i, len(sp.xy), dynamic=False)  # THIS SETS FRAME_SS

            for sp_id, sp in sh.sps.items():
                if sp.drawn != 0 and sp.f == None:
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
                        # try:
                        im_ax[sp.index_im_ax].set_color((sp.R[sp.clock], sp.G[sp.clock], sp.B[sp.clock]))
                        # except:
                        #     adf =5
                        im_ax[sp.index_im_ax].set_alpha(sp.alphas[sp.clock])
                        # im_ax[sp.index_im_ax].set_alpha(1)

                    elif drawBool == 2:
                        decrement_all_index_im_ax(index_removed, shs)
                        continue

        if P.A_SRS and 'srs' in sh.gi.child_names:
            if i in sh.gi.srs_gi['init_frames']:
                sr = sh.find_free_obj(type='sr')
                if sr != None and sr.id not in sr.gi['sr_hardcoded']:
                    prints += "  adding sr"
                    exceeds_frame_max, how_many = sr.check_frame_max(i, sr.gi['frames_tot'])
                    if exceeds_frame_max == True:
                        # prints += "  smoka exceeds max"
                        sr.frames_tot = how_many
                        # continue
                    sr.drawn = 1  # this variable can serve multiple purposes (see below, and in set_clock)
                    sh.sr_latest_drawn_id = sr.id
                    sr.init_child_obj(i, sr.gi['frames_tot'], dynamic=False)  # uses AbstractSSS
                    # f.gen_dyn_extent_alpha()

                else:
                    prints += "  no free sr"

            for sr_id, sr in sh.srs.items():

                if sr.drawn != 0:  # the 4 from above is needed only the very first iteration it becomes visible
                    sr.set_clock(i)

                    drawBool, index_removed = sr.ani_update_step(ax0, im_ax)
                    if drawBool == 0:  # dont draw
                        continue
                    elif drawBool == 1:
                        # warp_affine_and_color(i, ax0, im_ax, f, ch)  # parent obj required for sail
                        # print(im_ax[f.index_im_ax].get_alpha())
                        mpl_affine(i, sr, ax0, im_ax)
                        im_ax[sr.index_im_ax].set_alpha(sr.alpha[sr.clock])
                        # im_ax[sr.index_im_ax].set_alpha(1)
                    elif drawBool == 2:  # remove
                        decrement_all_index_im_ax(index_removed, shs)

        if P.A_RS and 'rs' in sh.gi.child_names:
            if i in sh.gi.rs_gi['init_frames']:
                r = sh.find_free_obj(type='r')
                if r != None and r.id not in r.gi['rs_hardcoded']:
                    prints += "  adding r"
                    exceeds_frame_max, how_many = r.check_frame_max(i, r.gi['frames_tot'])
                    if exceeds_frame_max == True:
                        # prints += "  smoka exceeds max"
                        r.frames_tot = how_many
                        # continue
                    r.drawn = 1  # this variable can serve multiple purposes (see below, and in set_clock)
                    # sh.rs_latest_drawn_id = r.id
                    r.init_child_obj(i, r.gi['frames_tot'], dynamic=False)  # uses AbstractSSS
                    # f.gen_dyn_extent_alpha()

                else:
                    prints += "  no free sr"

            for r_id, r in sh.rs.items():

                if r.drawn != 0:  # the 4 from above is needed only the very first iteration it becomes visible
                    r.set_clock(i)

                    drawBool, index_removed = r.ani_update_step(ax0, im_ax)
                    if drawBool == 0:  # dont draw
                        continue
                    elif drawBool == 1:
                        # warp_affine_and_color(i, ax0, im_ax, r)  # parent obj required for sail
                        # im_ax[r.index_im_ax].set_extent(r.extent[r.clock])  # parent obj required for sail
                        # print(im_ax[f.index_im_ax].get_alpha())
                        mpl_affine(i, r, ax0, im_ax)
                        # im_ax[r.index_im_ax].set_color((r.R[r.clock], r.G[r.clock], r.B[r.clock]))
                        # im_ax[r.index_im_ax].set(interpolation_stage='rgba', cmap='jet')
                        im_ax[r.index_im_ax].set_alpha(r.alpha[r.clock])
                        im_ax[r.index_im_ax].set_zorder(100)
                    elif drawBool == 2:  # remove
                        decrement_all_index_im_ax(index_removed, shs)

        if P.A_LS and 'ls' in sh.gi.child_names:
            if i in sh.gi.ls_gi['init_frames']:
                l = sh.find_free_obj(type='l')
                if l != None:
                    prints += "  adding l"
                    exceeds_frame_max, how_many = l.check_frame_max(i, l.gi['frames_tot'])
                    if exceeds_frame_max == True:
                        # prints += "  smoka exceeds max"
                        l.frames_tot = how_many
                        # continue
                    l.drawn = 1  # this variable can serve multiple purposes (see below, and in set_clock)
                    # sh.rs_latest_drawn_id = r.id
                    l.init_child_obj(i, l.gi['frames_tot'], dynamic=False)  # uses AbstractSSS
                    # f.gen_dyn_extent_alpha()

                else:
                    prints += "  no free ls"

            for l_id, l in sh.ls.items():

                if l.drawn != 0:  # the 4 from above is needed only the very first iteration it becomes visible
                    l.set_clock(i)

                    drawBool, index_removed = l.ani_update_step(ax0, im_ax)
                    if drawBool == 0:  # dont draw
                        continue
                    elif drawBool == 1:
                        # warp_affine_and_color(i, ax0, im_ax, r)  # parent obj required for sail
                        im_ax[l.index_im_ax].set_extent(l.extent[l.clock])  # parent obj required for sail
                        # print(im_ax[f.index_im_ax].get_alpha())
                        # mpl_affine(i, l, ax0, im_ax)
                        # im_ax[r.index_im_ax].set_color((r.R[r.clock], r.G[r.clock], r.B[r.clock]))
                        # im_ax[r.index_im_ax].set(interpolation_stage='rgba', cmap='jet')
                        im_ax[l.index_im_ax].set_alpha(l.alpha[l.clock])
                        # im_ax[l.index_im_ax].set_alpha(1)
                        im_ax[l.index_im_ax].set_zorder(100)
                    elif drawBool == 2:  # remove
                        decrement_all_index_im_ax(index_removed, shs)

        print(prints)

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
