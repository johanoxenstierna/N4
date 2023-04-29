import math
import numpy as np

# input parameters
height = float(100)
v = float(0)
theta = math.radians(0)
gravity = 9.81

# calculate time of flight
time = math.sqrt((2 * height) / gravity)
time = np.linspace(0, 30, num=30)

# calculate horizontal and vertical components of v
v_x = v * math.cos(theta)
v_y = v * math.sin(theta)

y_coords = np.zeros((len(time),))

# calculate horizontal and vertical distances travelled
for i in range(len(time)):
	# x_dist = v_x * time
	# y_dist = (v_y * time) - (0.5 * gravity * time * time)
	t = time[i]
	y_dist = (v_y * t) - (0.5 * gravity * t * t)
	y_coords[i] = y_dist

# print results
print("Coordinates of the object after", round(time, 2), "seconds:")
print("X-coordinate:", round(x_dist, 2))
print("Y-coordinate:", round(y_dist, 2))