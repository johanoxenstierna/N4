import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.pyplot import imread


def shift(y_sought, y):
    """y_sought is just the pixel y sought"""


    return y


g = 9.8


# try:
#     u = float(input('Enter initial velocity (m/s): '))
#     theta = float(input('Enter angle (deg): '))
# except ValueError:
#     print('Invalid input.')
# else:
#     theta = np.deg2rad(theta)
md = imread('./images/processed/mdoom3_small.png')  # 482, 187

u = 20
theta = -np.pi/4

t_flight = 2*u*np.sin(theta)/g
t = np.linspace(0, t_flight, 100)
x = u*np.cos(theta)*t
# x = x[20:]
y = u*np.sin(theta)*1*t - 0.5*g*t**2
# y_shift = y[20]
# y = y[20:]
# y -= y_shift

fig, ax = plt.subplots()
ax.imshow(md, zorder=1, alpha=1, origin='upper')
# ax.invert_yaxis()
# ax.axis([0, 254, 0, 133])
line, = ax.plot(x, y, color='yellow')

xmin = x[0]
ymin = y[0]
xmax = max(x)
ymax = max(y)
xysmall = min(xmax,ymax)
maxscale = max(xmax,ymax)
circle = plt.Circle((xmin, ymin), radius=np.sqrt(xysmall + 10))
# circle = plt.Polygon([(xmin, ymin)])
ax.add_patch(circle)

def animate(i, x, y, line, circle):
    if i < 6:
        line.set_data(x[:i], y[:i])
    else:
        line.set_data(x[i-5:i], y[i-5:i])
    line.set_alpha(0.5)
    line.set_color('#aabbcc')
    circle.center = x[i], y[i]  # THIS WORKS, USE PERHAPS WITH SMALL RADIUS
    # circle.set_data(x[i], y[i])
    # line.axes.axis([0, max(np.append(x, y)), 0, max(np.append(x,y))])

    return line,circle

ani = animation.FuncAnimation(fig, animate, len(x), fargs=[x, y, line, circle],
                              interval=25, blit=True)
#
# # ani.save('projectile.gif')
plt.show()