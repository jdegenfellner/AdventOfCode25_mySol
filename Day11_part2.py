import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# wrong: 285994866937104 (multiplied paths from svr to fft, fft to dac and dac to out)
# your answer is too low

# correct: 303012373210128

# need you to find every path from svr (the server rack) to out.
# However, the paths you find must all also visit BOTH dac and fft (in any order).

# input_Day11_test.txt

# svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out

# we need to read the input into a dictionary and then key (order it alphabetically) with
# the first 3 digits before the ":"

# read input

#with open('input_Day11_test_part2.txt') as f:
with open('input_Day11.txt') as f:
    lines = f.readlines()
# parse input
graph = {}
for line in lines:
    node, neighbors = line.strip().split(':')
    graph[node.strip()] = neighbors.strip().split(' ')

#print("graph:", graph)

# Visualize the graph structure
# highlight dac, fft, srv, out
G = nx.DiGraph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)
pos = nx.spring_layout(G)
node_colors = []
for node in G.nodes():
    if node in ['dac', 'fft']:
        node_colors.append('orange')
    elif node in ['svr', 'out']:
        node_colors.append('lightgreen')
    else:
        node_colors.append('lightblue')
nx.draw(G, pos, with_labels=True, node_color=node_colors, arrows=True)
plt.show()

# are there cycles in the graph?
cycles = list(nx.simple_cycles(G))
print("Cycles in the graph:", cycles)

# convert to adjacency matrix
nodes = list(G.nodes())
A = nx.to_numpy_array(G, nodelist=nodes, dtype=np.int64)

svr = nodes.index("svr")
fft = nodes.index("fft")
dac = nodes.index("dac")

# function to find number of paths of length m to n from node u to node v
def count_paths(A, u, v, length):
    Ak = np.linalg.matrix_power(A, length)
    return Ak[u, v]

# the overall path length was, if I remember correctly, 30-40 max.

# Part 1 - count all paths from svr to fft of length up to max_length
print("PART 1")
max_length = 40  # arbitrary limit to avoid infinite loops in cyclic graphs
total_paths_svr_to_fft = 0
for length in range(1, max_length + 1):
    paths = count_paths(A, svr, fft, length)
    print("length:", length, "; number of paths:", paths)
    total_paths_svr_to_fft += paths
print("Total paths from svr to fft:", total_paths_svr_to_fft)
# length 10: 608
# length 13: 10218
# Total paths from svr to fft: 10826

# Part 2 - count all paths from fft to dac of length up to max_length:
print("PART 2")
max_length = 40
dac = nodes.index("dac")
total_paths_fft_to_dac = 0
for length in range(1, max_length + 1):
    paths = count_paths(A, fft, dac, length)
    print("length:", length, "; number of paths:", paths)
    total_paths_fft_to_dac += paths
print("Total paths from fft to dac:", total_paths_fft_to_dac)

# length: 14 ; number of paths: 171592
# length: 15 ; number of paths: 1405988
# length: 16 ; number of paths: 2589978
# Total paths from fft to dac: 4167558

# Part 3 - count all paths from dac to out of length up to max_length:
print("PART 3")
max_length = 40
out = nodes.index("out")
total_paths_dac_to_out = 0
for length in range(1, max_length + 1):
    paths = count_paths(A, dac, out, length)
    print("length:", length, "; number of paths:", paths)
    total_paths_dac_to_out += paths
print("Total paths from dac to out:", total_paths_dac_to_out)
#length: 9 ; number of paths: 6716


# Part 4 - dac to fft:
print("PART 4")
max_length = 40
total_paths_dac_to_fft = 0
for length in range(1, max_length + 1):
    paths = count_paths(A, dac, fft, length)
    print("length:", length, "; number of paths:", paths)
    total_paths_dac_to_fft += paths
print("Total paths from dac to fft:", total_paths_dac_to_fft)
# Total paths from dac to fft: 0



# Final calculation:
final_count = (total_paths_svr_to_fft *
               total_paths_fft_to_dac *
               total_paths_dac_to_out)
print("Final count of paths from 'svr' to 'out' visiting both 'dac' and 'fft':", final_count)

# find all paths from svr to out of length up to max_length:
#max_length = 40
#out = nodes.index("out")
#total_paths_svr_to_out= 0
#for length in range(26, max_length + 1):
#    paths = count_paths(A, svr, out, length)
#    print("length:", length, "; number of paths:", paths)
#    total_paths_svr_to_out += paths
#print("Total paths from svr to out:", total_paths_svr_to_out)

# length: 29 ; number of paths: 9094196761732
# length: 30 ; number of paths: 98662085811067
# length: 31 ; number of paths: 551113827506065
# length: 32 ; number of paths: 2717690120337155
# length: 33 ; number of paths: 8922253661092182
# length: 34 ; number of paths: 24793685543944689
# length: 35 ; number of paths: 51500678056379667
# length: 36 ; number of paths: 72076857237592623
# length: 37 ; number of paths: 79915299682941478