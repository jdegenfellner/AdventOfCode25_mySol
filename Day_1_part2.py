def read_instructions_from_file(filename):
    with open(filename, 'r') as file:
        instr = [line.strip() for line in file.readlines()]
        #print(instructions[0:10])
        #print(len(instructions))
    return instr

def dissect_instruction(instruction):
    direction = instruction[0]
    steps = int(instruction[1:])
    return direction, steps

instructions = read_instructions_from_file('input.txt')
starting_position = 50 # static starting position
position = starting_position # dynamic position
zero_position_counter = 0

for instruction in instructions:
    direction, steps = dissect_instruction(instruction)
    print(f"Instruction: {instruction}, Direction: {direction}, Steps: {steps}")
    while steps > 0:
        if position == 0:
            zero_position_counter += 1
        if direction == 'L':
            position -= 1
            if position == -1:
                position = 99
        elif direction == 'R':
            position += 1
            if position == 100:
                position = 0
        steps -= 1

    print(f"New position: {position}, Zero position counter: {zero_position_counter}")



