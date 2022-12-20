import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from matplotlib.pyplot import imread


def get_image():
    Z = imread('./images/processed/0/0_f_1.png')  # 482, 187
    # delta = 0.25
    # x = y = np.arange(-3.0, 3.0, delta)
    # X, Y = np.meshgrid(x, y)
    # Z1 = np.exp(-X**2 - Y**2)
    # Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
    # Z = (Z1 - Z2)


    return Z




# prepare image and figure
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig, ax = plt.subplots(1,1)
Z = get_image()

im = ax.imshow(Z, interpolation='none',
                   origin='upper', extent=[-0, 6, 0, 6],
                   clip_on=False)

# im = ax.imshow(Z, origin='lower', clip_on=True)

trans_data = mtransforms.Affine2D().translate(5, 5) + ax.transData
# im.set_transform(trans_data)

# display intended extent of the image
x1, x2, y1, y2 = im.get_extent()
# ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "y--",
#         transform=trans_data)

ax.set_xlim(-15, 15)
ax.set_ylim(-14, 14)


# image rotation

# do_plot(ax, Z, mtransforms.Affine2D().rotate_deg(30))

# # image skew
# do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))
#
# # scale and reflection
# do_plot(ax, Z, mtransforms.Affine2D().scale(-1, .5))
#
# # everything and a translation
# do_plot(ax4, Z, mtransforms.Affine2D().
#         rotate_deg(30).skew_deg(30, 15).scale(-1, .5).translate(.5, -1))

plt.show()