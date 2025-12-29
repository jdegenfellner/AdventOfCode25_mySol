# input_Day12_test.txt looks like this:
# 0:
# ###
# ##.
# ##.
#
# 1:
# ###
# ##.
# .##
#
# 2:
# .##
# ###
# ##.
#
# 3:
# ##.
# ###
# ##.
#
# 4:
# ###
# #..
# ###
#
# 5:
# ###
# .#.
# ###
#
# 4x4: 0 0 0 0 2 0
# 12x5: 1 0 1 0 2 2
# 12x5: 1 0 1 0 3 2

# Read lines:
# format: "Digit[0 to 5]:", then 3 lines of 3 characters (# or .), then a blank line
# then a line with dimensions and counts: "WxH: c0 c1 c2 c3 c4 c5"

# read patterns and dimensions separately:

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    patterns = {}
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.endswith(':'):
            digit = int(line[:-1])
            pattern = []
            for j in range(1, 4):
                pattern.append(lines[i + j].strip())
            patterns[digit] = pattern
            i += 5  # Skip the blank line
        else:
            break
    dimensions = []
    while i < len(lines):
        line = lines[i].strip()
        if line:
            dim_part, counts_part = line.split(':')
            width, height = map(int, dim_part.split('x'))
            counts = list(map(int, counts_part.strip().split()))
            dimensions.append((width, height, counts))
        i += 1
    return patterns, dimensions # dimensions contains dimensions and required counts

#patterns, dimensions = read_input('input_Day12_test.txt') # for testing
patterns, dimensions = read_input('input_Day12.txt')
print("Patterns:")
for digit, pattern in patterns.items():
    print(f"{digit}:")
    for line in pattern:
        print(line)
print("\nDimensions and Counts:")
for dim in dimensions:
    print(dim)

# function to count '#' in a pattern
def count_hashes(pattern):
    return sum(line.count('#') for line in pattern)

# the trivial thing is to check if the packing is at all possible:
# if there are more '#' needed than available area, it's impossible
def can_pack(dimensions, patterns):
    impossible = []
    for width, height, counts in dimensions:
        total_area = width * height
        total_needed = sum(counts[digit] * count_hashes(patterns[digit]) for digit in range(6))
        if total_needed > total_area:
            print(f"Cannot pack for dimensions {width}x{height} with counts {counts}: "
                  f"needed at least {total_needed}, available {total_area}")
            # remember impossible cases
            impossible.append((width, height, counts))
        else:
            print(f"Can pack for dimensions {width}x{height} with counts {counts}: "
                  f"needed at least {total_needed}, available {total_area}")
    return impossible

impossible = can_pack(dimensions, patterns)

print("len dimensions before:", len(dimensions))

# remove impossible cases from dimensions and counts
dimensions_reduced = [dim for dim in dimensions if dim not in impossible]
print("len dimensions after:", len(dimensions_reduced))

# len dimensions before: 1000
# len dimensions after: 548

# -> This reduced the problem set nicely.

#again:
can_pack(dimensions_reduced, patterns)

# tried 548 as solution -> correct :)