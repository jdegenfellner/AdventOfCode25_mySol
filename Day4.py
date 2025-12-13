# make a matrix out of the input
# then go through all positions of the matrix and count if there are less than 4
# rolls of paper in the 8 adjacent positions

import numpy as np

 # read lines from file and create 2-dimensional array
def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        # define array with proper dimensions
        matrix = np.zeros((len(lines), len(lines[0])), dtype=str)
        # fill the array
        for i, line in enumerate(lines):
            for j, ch in enumerate(line):
                matrix[i][j] = ch
    return matrix

matrix = read_matrix_from_file('input_day4.txt')
print(matrix)
print(matrix[1][1])
print(matrix[1][:])
print(matrix[0][9])
#print(matrix.shape)

# parse the matrix:
# *) corners first
# *) all 4 margins
# *) then the inner matrix

def count_adjacent_rolls(matrix, i, j):
    rows, cols = matrix.shape
    count = 0

    if i==0 and j==0:
    # top-left corner
        adjacent_positions = [(0,1), (1,0), (1,1)]
    elif i==0 and j==cols-1:
    # top-right corner
        adjacent_positions = [(0,cols-2), (1,cols-1), (1,cols-2)]
    elif i==rows-1 and j==0:
    # bottom-left corner
        adjacent_positions = [(rows-2,0), (rows-1,1), (rows-2,1)]
    elif i==rows-1 and j==cols-1:
    # bottom-right corner
        adjacent_positions = [(rows-2,cols-1), (rows-1,cols-2), (rows-2,cols-2)]
    elif i==0 and 0 < j < cols-1:
    # top margin
        adjacent_positions = [(0,j-1), (0,j+1), (1,j-1), (1,j), (1,j+1)]
    elif i==rows-1 and 0 < j < cols-1:
    # bottom margin
        adjacent_positions = [(rows-1,j-1), (rows-1,j+1),
                              (rows-2,j-1), (rows-2,j),
                              (rows-2,j+1)]
    elif j==0 and 0 < i < rows-1:
    # left margin
        adjacent_positions = [(i-1,0), (i+1,0), (i-1,1), (i,1), (i+1,1)]
    elif j==cols-1 and 0 < i < rows-1:
    # right margin
        adjacent_positions = [(i-1,cols-1), (i+1,cols-1),
                              (i-1,cols-2), (i,cols-2),
                              (i+1,cols-2)]
    else:
    # inner matrix
        adjacent_positions = [(i-1,j-1), (i-1,j), (i-1,j+1),
                              (i,j-1),            (i,j+1),
                              (i+1,j-1), (i+1,j), (i+1,j+1)]
    # count rolls of paper in adjacent positions
    for pos in adjacent_positions:
        r, c = pos
        if matrix[r][c] == '@':
            count += 1
    return count

#test
matrix_with_x_marks = np.copy(matrix)
x_count = 0
for i in range(0,matrix.shape[0]):
    for j in range(0,matrix.shape[1]):
        cnt = count_adjacent_rolls(matrix, i, j)
        #if i==2:
            #print(f'Row 0, Col {j}, Count: {cnt}')
        if cnt < 4 and matrix[i][j] == '@':
            matrix_with_x_marks[i][j] = 'X'
            x_count += 1

print('------------')
print(matrix_with_x_marks)
print(f'Total X marks: {x_count}')