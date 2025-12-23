import numpy as np

# create empty array:
array = np.array([])

# read in input_Day9_test.txt, line by line, add to array,
# x,y coordinates separated by comma
with open('input_Day9.txt', 'r') as f:
    for line in f:
        x, y = line.strip().split(',')
        array = np.append(array, [[int(x), int(y)]], axis=0) if array.size else np.array([[int(x), int(y)]])

print(array)

# simple strategy:

# define function to calculate rectangle area given two diagonal points
# define a function to determine if two points are valid diagnoal points to form a rectangle
def is_valid_diagonal(p1, p2):
    return p1[0] != p2[0] and p1[1] != p2[1]

def rectangle_area(p1, p2):
    if not is_valid_diagonal(p1, p2):
        return 0
    length = abs(p1[0] - p2[0]) + 1
    width = abs(p1[1] - p2[1]) + 1
    return length * width

# tets with points 7,1 and 11,7:
p1 = np.array([7, 1])
p2 = np.array([11, 7])
area = rectangle_area(p1, p2)
print(f"Area of rectangle formed by points {p1} and {p2} is: {area}")

# calculate all areas for valid diagonal point pairs in the array
max_area = 0
num_points = array.shape[0]
for i in range(num_points):
    for j in range(i + 1, num_points):
        p1 = array[i]
        p2 = array[j]
        area = rectangle_area(p1, p2)
        if area > max_area:
            max_area = area
print(f"Maximum rectangle area from given points is: {max_area}")
print("points:", p1, p2)

# correct!
# 4741848414