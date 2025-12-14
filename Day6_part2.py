#file_to_use = "input_Day6_test.txt"
file_to_use = "input_Day6.txt"

# check if all elements in the column are " "
def all_elements_are_spaces(col_elements):
    for element in col_elements:
        if element != " ":
            return False
    return True

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

# eliminate newline characters
def clean_input(lines):
    cleaned_lines = [line.strip('\n') for line in lines]
    return cleaned_lines

cleaned_lines = clean_input(read_input(file_to_use)[:-1])
print(cleaned_lines)

# get math ops
math_ops = read_input(file_to_use)[-1]
math_ops = list(math_ops.replace(" ", ""))
print("math ops: ", math_ops)

# delete any \n from math_ops
math_ops = [op for op in math_ops if op != '\n']

num_of_cols = len(cleaned_lines[0])
print(num_of_cols)
number_of_rows = len(cleaned_lines)
print(number_of_rows)

def get_col_elements(col_index, cleaned_lines):
    col_elements = []
    for row_index in range(number_of_rows):
        element = cleaned_lines[row_index][col_index]
        col_elements.append(element)
    return col_elements

# function to create number from column elements deleting " " and concatenating digits
def create_number_from_col_elements(col_elements):
    digits = [element for element in col_elements if element != " "]
    number_str = ''.join(digits)
    if number_str == "":
        return None
    return int(number_str)
#test
print(create_number_from_col_elements([' ', '1', '2', ' '])) # 12

# go from right to left and calculate numbers to apply math ops on:
numbers_in_block = []
list_numbers_blocks = []
for col in range(num_of_cols -1, -1, -1):
    col_elements = get_col_elements(col, cleaned_lines)
    #print("col elements at index ", col, ": ", col_elements)
    if all_elements_are_spaces(col_elements):
        #print("all elements are spaces, number finished at column index: ", col)
        list_numbers_blocks.append(numbers_in_block)
        numbers_in_block = []
        continue
    else:
        # create number from column elements
        num = create_number_from_col_elements(col_elements)
        #print("number formed at column index ", col, ": ", num)
        numbers_in_block.append(num)
list_numbers_blocks.append(numbers_in_block)

print("numbers extracted: ", numbers_in_block)
print("list_numbers_blocks:", list_numbers_blocks)

# revers ops
math_ops.reverse()
print("reversed math ops: ", math_ops)

# build sums
sums = []
for i in range(len(list_numbers_blocks)):
    block = list_numbers_blocks[i]
    if len(block) == 0:
        continue
    op = math_ops[i]
    #print("block: ", block, " with op: ", op)
    block_res = 0
    for number in block:
        if op == '+':
            block_res += number
        elif op == '*':
            if block_res == 0:
                block_res = number
            else:
                block_res *= number
    sums.append(block_res)

print("block result: ", sums)

# final result
final_res = 0
for s in sums:
    final_res += s
print("final result: ", final_res)

# submitted: 3960210992996800
# That's not the right answer; your answer is too high.

# submitted: 9581313737063
# That's the right answer! You are one gold star closer to decorating the North Pole.