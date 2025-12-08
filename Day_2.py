# Identify the invalid product IDs
# They only have a few product ID ranges (your puzzle input) that you'll need to check

# The ranges are separated by commas (,); each range gives its first ID and last
# ID separated by a dash (-).

# Since the young Elf was just doing silly patterns, you can find the invalid
# IDs by looking for

#------------------
# !!!any ID which is made only of some sequence of digits repeated twice.!!!
#------------------

# So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
# None of the numbers have leading zeroes; 0101 isn't an ID at all
# 101 is a valid ID that you would ignore.

# Your job is to find all of the invalid IDs that appear in the given ranges.
# In the above example:

# The problem is to find repeating sequences which constitute the entire number.
# So, one needs to systematically check for all possible (i.e. divisors of the length)
# repeating sequences.

# For sanity check, one could first compute the number of searches that need to be done
# for a given range of IDs.

def read_id_ranges_from_file(filename):
    ranges = []
    vec = []
    with open(filename, 'r') as file:
        for line in file:
            range_current = line.split(",")
            ranges.append(range_current)
        for el in ranges:
            for single_el in el:
                vec.append(single_el)
        vec = [x for x in vec if "-" in x]
    return vec

def check_if_invalid_id(id_str):
    length = len(id_str)
    if length % 2 != 0:
        return False
    # now we know that length is even
    half_length = length // 2
    first_half = id_str[:half_length]
    second_half = id_str[half_length:]
    if first_half == second_half:
        return True
    return False

# check with 1010
#print(check_if_invalid_id("1010"))  # should be True
# check with 1188511885
#print(check_if_invalid_id("1188511885"))  # should be True

#test
#RANGES = read_id_ranges_from_file('input_day2_test.txt')
#print(f"ID Ranges: {RANGES}")
#print(f"Number of ID Ranges: {len(RANGES)}")

# determine invalid IDs in the given ranges
invalid_IDs = []
RANGES = read_id_ranges_from_file('input_day2.txt')
for r in RANGES:
    start_str, end_str = r.split("-")
    start_id = int(start_str)
    end_id = int(end_str)
    for current_id in range(start_id, end_id + 1):
        current_id_str = str(current_id)
        if check_if_invalid_id(current_id_str):
            invalid_IDs.append(current_id)

print(f"Invalid IDs: {invalid_IDs}")

# sum invalid IDs
sum_invalid_IDs = sum(invalid_IDs)
print(f"Sum of Invalid IDs: {sum_invalid_IDs}")
# worked with test input file!!

# Your puzzle answer was 55916882972.

