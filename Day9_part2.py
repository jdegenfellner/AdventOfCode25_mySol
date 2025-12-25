# wrong: 4666015710 (too high)
# wrong: 4660608106
# wrong: 4626743020
# wrong: 4643864427
# wrong: 4741848414
# wrong: 3156549294

# LOWER:
# wrong: 1587788048
# try: 1484192875
# try: 1399587145
# wrong: 1394849913
# try: 1278731904
# try: 1268907936

# UPPER:
# CORRECT!!!!!! 1508918480 !!!!!!!
# New max area 1508918480 found with points [ 6073 67455] and [94582, 50408]

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# create empty array:
array = np.array([])


# read in input_Day9_test.txt, line by line, add to array,
# x,y coordinates separated by comma
with open('input_Day9.txt', 'r') as f:
    for line in f:
        x, y = line.strip().split(',')
        array = np.append(array, [[int(x), int(y)]], axis=0) if array.size else np.array([[int(x), int(y)]])

print(array)

def is_valid_diagonal(p1, p2):
    return p1[0] != p2[0] and p1[1] != p2[1] # at least one coordinate must differ

def rectangle_area(p1, p2):
    if not is_valid_diagonal(p1, p2):
        return 0
    length = abs(p1[0] - p2[0]) + 1
    width = abs(p1[1] - p2[1]) + 1
    return length * width

# check if a point is inside the rectangle defined by p1 and p2
# for the lower part of the circle only
# we only need to check the lower part of the rectangle.
# if there is a point between the lower left point of the rectangle and
# the lower right point of the rectangle, with
# x coordinate between the two points
# then the rectangle is not valid
def is_valid_rectangle(p1, p2, point_set):
    x1, y1 = p1
    x2, y2 = p2
    x_min = min(x1, x2)
    x_max = max(x1, x2)
    y_min = min(y1, y2)
    # check all points in point_set
    for point in point_set:
        x, y = point
        if x_min < x < x_max and y == y_min: # inside.
            return False
    return True

# showPointsDay9.py shows us that the
# shape is NOT convex!!

# the two points disturbing the circle are:
# 94582,50408
# 94582,48356

# since the diagonal points still have to be part of the point set,
# we take one of these two points as fixed and choose the other diagonal point
# from the respective have.

# show x,y ranges in array
x = array[:, 0]
y = array[:, 1]
print(f"x range: {x.min()} to {x.max()}")
print(f"y range: {y.min()} to {y.max()}")

# filter array for lower points, lower rectangle (upper right point is fixed)
#filtered_array = array[
#    (array[:, 1] >= 30493) & (array[:, 1] <= 48356)
#]
# filter array for upper points, upper rectangle (lower right point is fixed)
filtered_array = array[
     (array[:, 1] >= 50408) & (array[:, 1] <= 68271)
 ]
print(f"Number of points in filtered array: {filtered_array.shape[0]}")
print(filtered_array)

# calculate all areas for valid diagonal point pairs in the filtered array
max_area = 0
num_points = filtered_array.shape[0]
min_x = filtered_array[:,0].min()
max_x = filtered_array[:,0].max()
min_y = filtered_array[:,1].min()
max_y = filtered_array[:,1].max()
# create grid for fast lookup

# max area for lower part:
for i in range(num_points):
    for j in range(i + 1, num_points):
        p1 = filtered_array[i]
        #p1 = [94582, 48356] # fixed for lower part
        p2 = [94582, 50408] # fixed for upper part
        #p2 = filtered_array[j]
        if not is_valid_diagonal(p1, p2):
            continue
        if not is_valid_rectangle(p1, p2, filtered_array):
            continue
        # check if the inside is filled with "X"s
        x1, y1 = p1
        x2, y2 = p2
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)

        area = rectangle_area(p1, p2)
        if area > max_area:
            print(f"New max area {area} found with points {p1} and {p2}")
            max_area = area
            max_p1 = p1
            max_p2 = p2

print(f"Maximum rectangle area from given points is: {max_area}")

# DRAW--------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# -----------------------
# Daten laden
# -----------------------
points = np.loadtxt("input_Day9.txt", delimiter=",", dtype=int)
x = points[:, 0]
y = points[:, 1]

# -----------------------
# Max-Area-Paare
# (ein Punkt ist immer gleich)
# -----------------------
# LOWER part:
#fixed_point = np.array([94582, 48356])
#other_points = np.array([
#    [5072, 34181],
#    [5072, 32774],
#    [5701, 31832],
#    [5701, 30493],
#])

# UPPER part:
fixed_point = np.array([94582, 50408])

other_points = np.array([
    [ 6073, 67455]
])


# -----------------------
# Plot
# -----------------------
fig, ax = plt.subplots(figsize=(7, 7))

ax.plot(x, y, color="tab:blue", linewidth=1, alpha=0.6)
ax.scatter(x, y, color="tab:blue", s=10, label="Path")

ax.scatter(
    fixed_point[0], fixed_point[1],
    s=140, facecolors="none", edgecolors="darkred",
    linewidths=3, label="Fixed lower point", zorder=10
)

for p in other_points:

    ax.scatter(
        p[0], p[1],
        s=120, facecolors="none", edgecolors="red",
        linewidths=2, zorder=10
    )

    ax.annotate(
        f"({p[0]}, {p[1]})",
        (p[0], p[1]),
        textcoords="offset points",
        xytext=(6, -10),
        fontsize=9,
        color="red"
    )

    x_min = min(fixed_point[0], p[0])
    y_min = min(fixed_point[1], p[1])
    width  = abs(fixed_point[0] - p[0])
    height = abs(fixed_point[1] - p[1])

    rect = Rectangle(
        (x_min, y_min),
        width, height,
        linewidth=2,
        edgecolor="red",
        facecolor="none",
        alpha=0.8
    )
    ax.add_patch(rect)

ax.set_aspect("equal")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Max-Area with fixed point")
ax.legend()
plt.show()