# The Elves are trying to figure out which junction boxes to connect
# so that electricity can reach every junction box. They even have a list of
# all of the junction boxes' positions in 3D space (your puzzle input).

# incorrect: 8!

from numpy.core.numeric import Inf
import numpy as np
import scipy.spatial.distance

# read file input_day8_test.txt as array, columns are separated by ",":
#file_path = "input_day8_test.txt"
file_path = "input_day8.txt"

with open(file_path, "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f]
    points_list = [list(map(int, line.split(","))) for line in lines]
    points = np.array(points_list) # array
    print(points)

print("Grid dimensions:", points.shape) # 20 x 3


#min_pair, min_dist = min_distance(dist_matrix)
#print("Minimum distance is between points", min_pair, "with distance", min_dist)
## print coordinates of the points with minimum distance
#print("Coordinates of the points with minimum distance:")
#print("Point 1:", points[min_pair[0]])
#print("Point 2:", points[min_pair[1]])
# -> correct

# function to check if two points are in the same circuit
def are_connected(point1, point2, list_of_circuits):
    for circuit in list_of_circuits:
        if point1 in circuit and point2 in circuit:
            return True
    return False

# test the function
#print("Are points 0 and 19 connected?", are_connected(0, 19, list_of_circuits)) # True
#print("Are points 0 and 1 connected?", are_connected(0, 1, list_of_circuits)) # False

#min_pair, min_dist = min_distance_not_connected(dist_matrix, list_of_circuits)
#print("Minimum distance between not connected points is between points", min_pair, "with distance", min_dist)
## print coordinates of the points with minimum distance
#print("Coordinates of the points with minimum distance not connected:")
#print("Point 1:", points[min_pair[0]])
#print("Point 2:", points[min_pair[1]])
# -> correct

# either of the min_pair is in a circuit, add the other to the same circuit
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

# test the function
#add_connection(min_pair, list_of_circuits)
#print("List of circuits after adding connection:", list_of_circuits)

# function to merge two circuits if the min distance is between points in different circuits:
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

print("----------- FOR TEST INPUT --------------")
condensed_distance_matrix = scipy.spatial.distance.pdist(points, metric='euclidean')
list_10_min_points = []
min_indices = np.argsort(condensed_distance_matrix)[:1000]
for index in min_indices:
    # convert index back to square distance matrix indices
    n = len(points)
    # formula to convert condensed index to square indices:
    # k = n * i - i * (i + 1) / 2 + j - i - 1
    # solve for i and j:
    k = index
    i = int(n - 2 - np.floor(np.sqrt(-8*k + 4*n*(n-1)-7)/2.0 - 0.5))
    j = int(k + i + 1 - n*(n-1)//2 + (n - i)*((n - i) - 1)//2)
    dist = condensed_distance_matrix[index]
    print("Points:", (i, j), "Distance:", dist)
    list_10_min_points.append((i, j, dist))

print("List of 10 minimum distance points:", list_10_min_points)

# now we build the circuits.
# we go through the list of minimum distance points and add connections
# if two points are already connected, we skip them.
# if neither point is in a circuit, we create a new circuit containing the two points.
# if only one point is already in a circuit, we add the other point to the same circuit.
list_of_circuits = []
counter = 0
for point1, point2, dist in list_10_min_points:
    counter += 1
    print("counter:", counter)
    merge_circuits(point1, point2, list_of_circuits)
    if not are_connected(point1, point2, list_of_circuits):
        add_connection((point1, point2), list_of_circuits)
        print("Connecting points", (point1, point2), "with distance", dist)
        print("Coordinates:")
        print("Point 1:", points[point1])
        print("Point 2:", points[point2])
        print("current list of circuits:", list_of_circuits)
    else:
        print("Points", (point1, point2), "are already connected, skipping.")

print("Final list of circuits:", list_of_circuits)

# lengths of circuits
circuit_lengths = [len(circuit) for circuit in list_of_circuits]
circuit_lengths.sort(reverse=True)
print("Lengths of circuits:", circuit_lengths)

# multiply lengths of the first 3 largest:
result = 1
for length in circuit_lengths[:3]:
    result *= length

print("Result (product of lengths of the 3 largest circuits):", result)

