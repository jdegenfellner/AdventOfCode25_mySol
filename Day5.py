# read lines from input_day5_test.txt and print them
with open('input_day5.txt', 'r') as file:
    lines = file.readlines()

print(lines)

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
print(numbers)

# which numbers fall within any of the ranges?
def is_in_ranges(number, ranges):
    for start, end in ranges:
        if start <= number <= end:
            return True
    return False

valid_numbers = [num for num in numbers if is_in_ranges(num, ranges)]
print("Valid numbers:", valid_numbers)
print(len(valid_numbers))