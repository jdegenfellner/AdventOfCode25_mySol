# To help the Elves figure out which path is causing the issue,
# they need you to find every path from you to out.

# example:
# aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out

# I think this is easy, we just need to systematically explore all paths from 'you' to 'out'.
# and count how often we reach 'out'.

# read input
with open('input_Day11.txt') as f:
    lines = f.readlines()
# parse input
nodes_list = []
neighbors_list = []
for line in lines:
    print(line)
    node, neighbors = line.strip().split(':')
    nodes_list.append(node.strip())
    neighbors_list.append(neighbors.strip().split(' '))

print("nodes_list:", nodes_list)
print("neighbors_list:", neighbors_list)

# we need a recursive function to explore all paths:
# we start at 'you' and explore all neighbors of 'you';
# then we go to each neighbor of the next node and explore its neighbors
# until we reach 'out';
# as soon as we reach 'out', we increment a counter.
def explore_paths(current_node, nodes_list, neighbors_list, path, all_paths):
    path.append(current_node)
    if current_node == 'out':
        all_paths.append(list(path))
    else:
        current_index = nodes_list.index(current_node)
        for neighbor in neighbors_list[current_index]:
            explore_paths(neighbor, nodes_list, neighbors_list, path, all_paths)
    path.pop()

all_paths = []
explore_paths('you', nodes_list, neighbors_list, [], all_paths)
print("All paths from 'you' to 'out':")
for p in all_paths:
    print(" -> ".join(p))
print("Total number of paths from 'you' to 'out':", len(all_paths))


# correct: 615