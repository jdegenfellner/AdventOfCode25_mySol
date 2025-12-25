
# the lines in the file input_Day10.txt and input_Day10_test.txt are formatted as follows:
# "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"

# the first part in [] represents the lights and the desired final state of the lights
# the second part in ()s represents the switches and which lights they control
# the last part in {} represents the number of times each switch can be toggled - THIS can be IGNORED for now

# single toggle like (3) should not contain a comma
# multiple toggles like (1,3) should contain a comma

# create function to read the file input_Day10.txt and parse each line into lights-list and switches-list
def parse_line(line):
    parts = line.strip().split(' ')
    lights_part = parts[0]
    switches_part = parts[1:-1]
    lights_target = [c == '#' for c in lights_part[1:-1]]
    lights_init = [False] * len(lights_target)  # all lights off initially
    switches = []
    for switch_str in switches_part:
        switch_str = switch_str[1:-1]  # remove parentheses
        if ',' in switch_str:
            indices = list(map(int, switch_str.split(',')))
        else:
            indices = [int(switch_str)]
        switches.append(indices)
    return lights_target, lights_init, switches

# function to apply a switch toggle to lights
def toggle_switch(lights, switch):
    for index in switch:
        lights[index] = not lights[index]
# True = on (#), False = off (.)

# now we need to find out how to reach the target lights state from the initial lights state
# first observation is that toggling the same switch twice cancels out its effect.

# mathematically, we are looking for a linear combination of the (binary) switch
# effects that equals the target state.

# function to check if current lights state matches target state
def lights_match(lights, target):
    return lights == target

# function to go through all 2^(number of combinations) combinations of switches applied to initial lights state
# to find the minimum number of toggles needed to reach target state
def find_min_toggles(lights_init, lights_target, switches):
    from itertools import product
    n = len(switches)
    min_toggles = float('inf')
    for toggle_pattern in product([0, 1], repeat=n): # brute force
        lights = lights_init[:]
        toggles_count = sum(toggle_pattern)
        for i in range(n):
            if toggle_pattern[i] == 1:
                toggle_switch(lights, switches[i])
        if lights_match(lights, lights_target):
            min_toggles = min(min_toggles, toggles_count)
    return min_toggles if min_toggles != float('inf') else None

# test with first:
#print(find_min_toggles( [False, False, False, False], [False, True, True, False],
#                       [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]]
#                        )
#      )

# test with second:
#print(find_min_toggles( [False, False, False, False, False],
#                         [False, False, False, True, False],
#                       [[0,2,3,4], [2,3], [0,4], [0,1,2], [1,2,3,4]]
#                        )
#      )

# test with third:
#print(find_min_toggles( [False, False, False, False, False, False],
#                         [False, True, True, True, False, True],
#                       [[0,1,2,3,4], [0,3,4], [0,1,2,4,5], [1,2]]
#                        )
#      )

# main-----------------
# list of number of minimum toggles for each switch:
min_number_of_toggles = []
with open('input_Day10.txt', 'r') as f:
    for line in f:
        lights_target, lights_init, switches = parse_line(line)
        min_toggles = find_min_toggles(lights_init, lights_target, switches)
        min_number_of_toggles.append(min_toggles)

#sum(min_number_of_toggles) to get final result for part 1
print("Final result:", sum(min_number_of_toggles))