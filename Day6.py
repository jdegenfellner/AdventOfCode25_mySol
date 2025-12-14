# read input_day6_test.txt:
# we are interested in the columns of the characters in the file.
# the last line are the math operations to be performed on the column-elements.
# the columns are separated by spaces.

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# ['123 328  51 64', '45 64  387 23', '6 98  215 314', '*   +   *   +']

# create columns from the input using all but the last line
def create_columns(lines):
    columns = []
    for line in lines[:-1]:
        elements = line.split()
        for i, element in enumerate(elements):
            if len(columns) <= i:
                columns.append([])
            columns[i].append(int(element))
    return columns

math_ops = read_input("input_Day6.txt")[-1]
math_ops = list(math_ops.replace(" ", ""))
columns = create_columns(read_input("input_Day6.txt"))

# for every element in the columns, perform the math operation specified in math_ops between the single column elements
def perform_operations(columns, math_ops):
    results = []
    for col_index, column in enumerate(columns):
        operation = math_ops[col_index]
        print("column: ", column, " operation: ", operation)
        result = column[0]
        for element in column[1:]:
            if operation == '+':
                result += element
            elif operation == '*':
                result *= element
            # add more operations if needed
        results.append(result)
    return results

results = perform_operations(columns, math_ops)
print(results)

# sum
final_result = sum(results)
print("Final result: ", final_result)