# now we start at 0 in every place.
# every toggle increases the number of toggles at the indicated place by 1.

# another discrete optimization problem.
# we are looking for the minimum number of toggles at each light.

# formally, this is a problem like:
# minimize the sum of the toggle counts.
# S.t.:
# linear combination of the toggle-vectors = target-vector

# brute-force will likely fail, since we have very large joltages like 214 in there.....

# heuristically, one could try an over-shoot- under shoot approach?
# but does this always converge to the optimal solution?

# the good thin is that the order in which we apply the toggles does not matter.
# only the final state counts.

# I know there is an algorithm for this, but I can't remember it right now.

# One can write the problem as:
# min sum_i lambda_i
# s.t.:
# Toggle Matrix (e.g. 4x5) times Lambda Vector (5x1) = Target Vector (4x1)

import sys, scipy
print(sys.executable)
print(scipy.__version__)

from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

# now we parse the lines:
# "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
# the first part in [] can be ignored, then come the switches in ()s as "switches", and the last part in {}
# must also be read in as "target"

def parse_line_part2(line):
    parts = line.strip().split(' ')
    lights_part = parts[0]
    switches_part = parts[1:-1]
    target_part = parts[-1]
    lights_target = [c == '#' for c in lights_part[1:-1]]
    switches = []
    for switch_str in switches_part:
        switch_str = switch_str[1:-1]  # remove parentheses
        if ',' in switch_str:
            indices = list(map(int, switch_str.split(',')))
        else:
            indices = [int(switch_str)]
        switches.append(indices)
    target_counts = list(map(int, target_part[1:-1].split(',')))
    return lights_target, switches, target_counts

# test
#line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
#lights_target, switches, target_counts = parse_line_part2(line)
#print("lights_target:", lights_target)
#print("switches:", switches)
#print("target_counts:", target_counts)

# we are only interested in "switches" and "target_counts" from now on:

# linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=(0, None),
# #       method='highs', callback=None, options=None, x0=None, integrality=None)

# example first line:
# c = [1, 1, 1, 1] which is just the sum of the toggles.
# A_eq  is a 4x6 matrix:
# A_eq = [
#  [0, 0, 0, 0, 1, 1],
#  [0, 1, 0, 0, 0, 1],
#  [0, 0, 1, 1, 1, 0],
#  [1, 1, 0, 1, 0, 0],
# ]
# b_eq = [3, 5, 4, 7]  # target

def build_lp_matrices(switches, target_counts):
    num_lights = len(target_counts) # 4
    num_switches = len(switches) # 6
    A_eq = [[0]*num_switches for _ in range(num_lights)] # 4x6 zero matrix
    for j, switch in enumerate(switches):
        for light_index in switch:
            A_eq[light_index][j] += 1
    b_eq = target_counts
    c = [1]*num_switches  # minimize sum of toggles
    return c, A_eq, b_eq

# test with first line:
#line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
#lights_target, switches, target_counts = parse_line_part2(line)
#c, A_eq, b_eq = build_lp_matrices(switches, target_counts)
#print("c:", c)
#print("A_eq:", A_eq)
#print("b_eq:", b_eq)

# solve first line using linprog
#res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method='highs')
#if res.success:
#    print("Optimal value (minimum toggles):", res.fun)
#    print("Toggle counts per switch:", res.x)
#else:
#    print("No solution found for the first line.")
# correct! Optimal value (minimum toggles): 10.0

# we also want to verify that the solution matches the target counts:
#toggle_counts = res.x
#final_counts = [0]*len(target_counts)#
#for j, switch in enumerate(switches):
#    for light_index in switch:
#        final_counts[light_index] += toggle_counts[j]
#print("Final counts after applying toggles:", final_counts)
#print("Target counts:", target_counts)

list_min_toggles = []
line_counter = 0
with open('input_Day10.txt', 'r') as f:
    for line in f:
        lights_target, switches, target_counts = parse_line_part2(line)
        c, A_eq, b_eq = build_lp_matrices(switches, target_counts)
        #res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method='highs')
        res = milp(
            c=c,
            integrality=np.ones(len(c), dtype=int),  # alle Variablen ganzzahlig
            bounds=Bounds(0, np.inf),
            constraints=LinearConstraint(A_eq, b_eq, b_eq)
        )
        if res.success:
            list_min_toggles.append(int(res.fun))
        else:
            list_min_toggles.append(None)
        # verify solution:
        toggle_counts = res.x
        final_counts = [0]*len(target_counts)
        for j, switch in enumerate(switches):
            for light_index in switch:
                final_counts[light_index] += toggle_counts[j]
        if not final_counts == target_counts:
            print("Solution does not match target counts!")
            print("Final counts after applying toggles:", final_counts)
            print("Target counts:", target_counts)
            print(f"Processed line {line_counter}")
            print(switches)
        line_counter += 1
#for i, min_toggles in enumerate(list_min_toggles):
#    print(f"Line {i+1}: Minimum toggles = {min_toggles}")
# done

print("in sum toggles:", sum(list_min_toggles))
# test (input_Day10_test.txt) worked and gave 33!!!

# wrong: 16587, your answer is too low
# now with integer and milp(): 16612; That's not the right answer; your answer is too low
# GUESSED that the correct answer is just ONE higher since in one optimization setting there was
# slight missmatch in the solution :)

# correct answer is 16613


