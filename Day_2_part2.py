# The clerk quickly discovers that there are still invalid IDs in the ranges in
# your list.
# Maybe the young Elf was doing other silly patterns as well?
#
# Now, an ID is invalid if it is made only of some sequence of digits repeated
# !!!at least twice!!!

# So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times),
# and 1111111 (1 seven times) are all invalid IDs.

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

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

def check_if_invalid_id_at_least_twice(id_str):
    length = len(id_str)
    divisors = get_divisors(length)
    #print(f"Divisors: {divisors}")
    for div in divisors:
        parts = [id_str[i:i+div] for i in range(0,len(id_str),div)]
        #print(parts)
        if len(set(parts)) == 1 and len(parts) >= 2:
            return True
    return False

# test
#print(check_if_invalid_id_at_least_twice("1010"))  # True
#print(len(['10', '10']))
#print(len(set(['10', '10'])))

#print(check_if_invalid_id_at_least_twice("123123123"))  # True
#print(check_if_invalid_id_at_least_twice("1188511885"))  #  True
#print(check_if_invalid_id_at_least_twice("222222222")) # True
#print(check_if_invalid_id_at_least_twice("16988")) # WRONG!!

# determine invalid IDs in the given ranges
invalid_IDs = []
RANGES = read_id_ranges_from_file('input_day2.txt')
for r in RANGES:
    start_str, end_str = r.split("-")
    start_id = int(start_str)
    end_id = int(end_str)
    for current_id in range(start_id, end_id + 1):
        current_id_str = str(current_id)
        if check_if_invalid_id_at_least_twice(current_id_str):
            invalid_IDs.append(current_id)

print(f"Invalid IDs: {invalid_IDs}")

# sum invalid IDs
sum_invalid_IDs = sum(invalid_IDs)
print(f"Sum of Invalid IDs: {sum_invalid_IDs}")
