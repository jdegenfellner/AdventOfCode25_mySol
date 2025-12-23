# https://github.com/jdegenfellner/AdventOfCode25_mySol

# The Elves were right; they definitely don't have enough extension cables. #
# You'll need to keep connecting junction boxes together until they're all in one large circuit.
#
# Continuing the above example, the first connection which causes all of the junction
# boxes to form a single circuit is between the junction boxes at 216,146,977 and 117,168,530.
# The Elves need to know how far those junction boxes are from the wall so they can pick the
# right extension cable; multiplying the X coordinates of those two junction boxes
# (216 and 117) produces 25272.
#
# Continue connecting the closest unconnected pairs of junction boxes together until
# they're all in the same circuit. What do you get if you multiply together the X
# coordinates of the last two junction boxes you need to connect?

import numpy as np
import scipy.spatial.distance
from scipy.spatial.distance import pdist, squareform

# read file input_day8_test.txt as array, columns are separated by ",":
#file_path = "input_day8_test.txt"
file_path = "input_day8.txt"

with open(file_path, "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f]
    points_list = [list(map(int, line.split(","))) for line in lines]
    points = np.array(points_list) # array
    #print(points)
#print("Grid dimensions:", points.shape) # 20 x 3

def are_connected(point1, point2, list_of_circuits):
    for circuit in list_of_circuits:
        if point1 in circuit and point2 in circuit:
            return True
    return False

def merge_circuits(point1, point2, list_of_circuits):
    circuit1 = None
    circuit2 = None
    for circuit in list_of_circuits:
        if point1 in circuit:
            circuit1 = circuit
        if point2 in circuit:
            circuit2 = circuit
    if circuit1 is not None and circuit2 is not None and circuit1 != circuit2:
        circuit1.update(circuit2)
        list_of_circuits.remove(circuit2)
        print("Merged circuits containing points", point1, "and", point2)
        print("Coordinates:; Point 1:", points[point1], "; Point 2:", points[point2])

def add_connection(min_pair, list_of_circuits):
    point1, point2 = min_pair
    for circuit in list_of_circuits:
        if point1 in circuit:
            circuit.add(point2)
            return
        if point2 in circuit:
            circuit.add(point1)
            return
    # if neither point is in a circuit, create a new circuit
    list_of_circuits.append({point1, point2})

condensed_distance_matrix = scipy.spatial.distance.pdist(points, metric='euclidean')
D = squareform(pdist(points, metric="euclidean"))  # NxN
n = len(points)

edges = []
for i in range(n):
    for j in range(i+1, n):
        edges.append((D[i, j], i, j))

edges.sort(key=lambda x: x[0])  # sort by distance
print("edges sorted by distance:", edges)

# now we build the circuits:
list_of_circuits = []
for dist, point1, point2 in edges:
    # merge circuits if needed:
    merge_circuits(point1, point2, list_of_circuits)
    if len(list_of_circuits) == 1 and len(list_of_circuits[0]) == n:
        print("-> All points are now connected in a single circuit.")
        print("Last points:", (point1, point2))
        print("Coordinates:; Point 1:", points[point1], "; Point 2:", points[point2])
        print("Final list of circuits:", list_of_circuits)
        print("product of X coordinates of last connected points:", points[point1][0] * points[point2][0])
        break

    # merge points to circuits or points to each other in pairs:
    if not are_connected(point1, point2, list_of_circuits):
        add_connection((point1, point2), list_of_circuits)
        print("Connecting points", (point1, point2), "with distance", dist)
        print("Coordinates:; Point 1:", points[point1], "; Point 2:", points[point2])
        print("current list of circuits:", list_of_circuits)
        if len(list_of_circuits) == 1 and len(list_of_circuits[0]) == n:
            print("-> All points are now connected in a single circuit.")
            print("Last connected points:", (point1, point2))
            print("Coordinates:; Point 1:", points[point1], "; Point 2:", points[point2])
            print("Final list of circuits:", list_of_circuits)
            print("product of X coordinates of last connected points:", points[point1][0] * points[point2][0])
            break
    else:
        print("Points", (point1, point2), "are already connected, skipping.")

    print("number of circuits: ", len(list_of_circuits))


# gpt gave me the idea that the criterion is wrong:
# if I exchange the condition "counter > 7" with "len(list_of_circuits[0]) == n",
# works in the training example, but why?
# ->it could be the case that we have a lot of points in one circuit, but not all points yet!
