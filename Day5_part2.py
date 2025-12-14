with open('input_day5.txt', 'r') as file:
    lines = file.readlines()

#print(lines)

# the data structure is
# ranges XX-YY,AA-BB, then an empty line, then a series numbers.
ranges = []
numbers = []
reading_ranges = True
for line in lines:
    line = line.strip()
    if line == "":
        reading_ranges = False
        continue
    if reading_ranges:
        parts = line.split(',')
        for part in parts:
            start, end = map(int, part.split('-'))
            ranges.append((start, end))
    else:
        numbers.append(int(line))

print(ranges)
#print(numbers)


# which numbers fall within any of the ranges?
def is_in_ranges(number, ranges):
    for start, end in ranges:
        if start <= number <= end:
            return True
    return False

valid_numbers = [num for num in numbers if is_in_ranges(num, ranges)]
#print("Valid numbers:", valid_numbers)
#print(len(valid_numbers))

print(len(ranges)) # 174 ranges?

# part2
# we need all unique numbers in the ranges

# listing all numbers in the ranges would be too large

# application of formula 15 (https://people.math.ethz.ch/~jteichma/slides_w_fs2021.pdf)
# seems also not easy since one would have many overlaps, for instance 174 over 2 in the first
# part of the sum.

# instead we calculate the number of unique numbers in the range
# by considering the overlaps.


# the nice thing is that I do not have to count the number of how often a number occurs,
# but only IF it occurs in any range!

# idea:
# find min and max of all ranges.

print(ranges[0][0])
print(ranges[0][1])

def min_max_ranges(ranges):
    min_value = min(ranges[i][0] for i in range(len(ranges)))
    max_value = max(ranges[i][1] for i in range(len(ranges)))
    return min_value, max_value
min_value, max_value = min_max_ranges(ranges)
print("Min and max of ranges:", min_value, max_value)

# this is our relevant space
# then every lower and upper bound of a range is a relevant point

# idiot solution - lets call this plan B :)
# count from min_value to max_value
#count = 0
#for number in range(min_value, max_value + 1):
#    if is_in_ranges(number, ranges):
#        count += 1
#        pass
#        # count it
#print(count)

# https://en.wikipedia.org/wiki/Sweep_line_algorithm

# better:
# put all relevant points into a list
# sort the list
# then go through the list and determine if the intervals defined by the points are covered by any range:
# an interval is by definition covered if there is an interval with start <= point1 and end >= point2

relevant_points = set()
for start, end in ranges:
    relevant_points.add(start)
    relevant_points.add(end)

relevant_points = sorted(relevant_points)
print("Relevant points:", relevant_points)
print(len(relevant_points)) # 284 (100 are omitted due to repetition) / 8 in test


# count only inner points, i.e., points between two relevant points
total_inner_points = 0
for i in range(len(relevant_points) - 1):

    point1 = relevant_points[i]
    point2 = relevant_points[i + 1]

    # count valid inner points
    for start, end in ranges:
        if start <= point1 + 1 and end >= point2 - 1:
            print("Interval", point1, "to", point2, "is covered by range", start, "-", end)
            inner_points = point2 - point1 - 1
            print("Inner points in this interval:", inner_points)
            break

    total_inner_points += inner_points
    inner_points = 0

print("Total inner points covered:", total_inner_points)

# count single points, each exactly once.
number_of_covered_numbers = 0
for point in relevant_points:
    # check if the point is covered by any range
    is_covered = False
    for start, end in ranges:
        if start <= point <= end:
            is_covered = True
            break
    if is_covered:
        number_of_covered_numbers += 1

print("Number of covered single points:", number_of_covered_numbers)

total_covered_numbers = total_inner_points + number_of_covered_numbers
print("Total number of covered numbers:", total_covered_numbers)




# submitted: 549068351461695
# That's not the right answer; your answer is too high.

# submitted: 348548952146313
# That's the right answer! You are one gold star closer to decorating the North Pole.