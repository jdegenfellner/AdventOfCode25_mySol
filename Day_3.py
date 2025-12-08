def read_banks_from_file(filename):
    with open(filename, 'r') as file:
        banks = [line.strip() for line in file.readlines()]
        #print(instructions[0:10])
        #print(len(instructions))
    return banks


#test
banks = read_banks_from_file('input_day3.txt')
print(banks)

def extract_single_digit_numbers(s):
    numbers = []
    for char in s:
        if char.isdigit():
            numbers.append(int(char))
    return numbers

def concatenate_single_digit_numbers(numb1, numb2):
    result = 0
    numb1 = int(numb1)
    numb2 = int(numb2)
    result = numb1 * 10 + numb2
    return result

# test


# now for every bank, we just need to go through the upper triangle matrix,
# concatenate the single digit numbers and compare it to the current maximum

def find_largest_code(bank):
    single_digit_numbers = extract_single_digit_numbers(bank)
    max_code = -1
    size = len(bank)
    for j in range(1,size):
        for i in range(0,j):
            current_number = concatenate_single_digit_numbers(single_digit_numbers[i], single_digit_numbers[j])
            if current_number > max_code:
                max_code = current_number
    return max_code

# test
print(find_largest_code('987654321111111'))
print(find_largest_code('811111111111119'))
print(find_largest_code('234234234234278'))
print(find_largest_code('818181911112111'))

overall_sum_largest_codes = 0

for bank in banks:
    largest_code = find_largest_code(bank)
    overall_sum_largest_codes += largest_code

print("Overall sum of largest codes:", overall_sum_largest_codes)