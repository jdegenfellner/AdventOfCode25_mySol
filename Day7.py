# You quickly locate a diagram of the tachyon manifold (your puzzle input).
# A tachyon beam enters the manifold at the location marked S; tachyon beams always move downward.
# Tachyon beams pass freely through empty space (.). However, if a tachyon beam encounters a splitter (^),
# the beam is stopped; instead, a new tachyon beam continues from the immediate left and from the immediate
# right of the splitter.

# note: there are exactly 21 splitter ins the test input, since one (last line) ist not hit.

#file_path = 'input_Day7_test.txt'
file_path = 'input_day7.txt'

# read file
with open(file_path, 'r') as file:
    lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    rows = len(grid)
    cols = len(grid[0])

# delete line breaks
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# show each line in a new row
for j in range(len(lines)):
    print(lines[j])

#print("rows: ", rows)
#print("cols: ", cols)
#print(lines)

# the algorithms seems rather solvable:
# - one iterates from the SECOND line to the last:
# - if there is an S, one starts a beam under it
# RULES:
# - if there is a ., the beam continues down
# - if there is a ^ below a beam, the beam stops, and two new beams start left and right of it
# before drawing a beam, check if there is already one.
# one needs to count the events where a beam hits a splitter (^)

#print(lines[1][5])  # should be .

split_counter = 0
for i in range(1, rows): # start from second line
    for j in range(cols):
        if lines[i-1][j] == 'S' or lines[i-1][j] == '|':  # S or beam above
            if lines[i][j] == '.':
                # continue beam down
                lines[i] = lines[i][:j] + '|' + lines[i][j+1:]
            elif lines[i][j] == '^':
                # hit splitter, stop beam, start new beams left and right
                split_counter += 1
                # stop current beam
                # start left beam
                if j > 0 and lines[i][j-1] != '|':
                    lines[i] = lines[i][:j-1] + '|' + lines[i][j:]
                # start right beam
                if j < cols - 1 and lines[i][j+1] != '|':
                    lines[i] = lines[i][:j+1] + '|' + lines[i][j+2:]

# show each line in a new row
for j in range(len(lines)):
    print(lines[j])

print("Number of splitters hit: ", split_counter)

# submitted: 1587
# That's the right answer!
