# You're actually supposed to count the number of times any click causes
# the dial to point at 0, regardless of whether it happens during a rotation
# or at the end of one.

def dissect_instruction(instruction):
    direction = instruction[0]
    steps = int(instruction[1:])
    return direction, steps

def apply_instruction(position, instruction):
    direction, steps = dissect_instruction(instruction)
    zero_crossings = 0
    remainder = steps % 100
    full_cycles = steps // 100
    print(f"remainder: {remainder}, full_cycles: {full_cycles}")

    # 1) determine how often we pointed to zero
    if direction == 'L':
        # distinguish between position == 0 and position > 0
        if position == 0:
            zero_crossings += full_cycles
        if position > 0:
            zero_crossings += (position - remainder < 0) + full_cycles
    elif direction == 'R':
        if position == 0:
            zero_crossings += full_cycles
        if position > 0:
            zero_crossings += (position + remainder > 99) + full_cycles

    # 2) determine new position in the circular track
    if direction == 'L':
        position -= steps
    elif direction == 'R':
        position += steps
    else:
        raise ValueError(f"Invalid direction: {direction}")

    while position < 0:
        position += 100
    while position >= 100:
        position -= 100

    is_zero_at_end_position = (position == 0)

    return position, is_zero_at_end_position, zero_crossings

def run_instructions(instr, start_pos):
    position = start_pos
    zero_count = 0
    zero_crossings_count = 0

    for instruction in instr:
        position, is_zero, zero_crossings = apply_instruction(position, instruction)
        zero_crossings_count += zero_crossings
        if is_zero:
            zero_count += 1
        print(f"After instruction {instruction}, position: {position}, zero_count: {zero_count}",
              f"zero_crossings_counter: {zero_crossings_count}")

    return position, zero_count, zero_crossings_count

def read_instructions_from_file(filename):
    with open(filename, 'r') as file:
        instr = [line.strip() for line in file.readlines()]
        #print(instructions[0:10])
        #print(len(instructions))
    return instr

instructions = read_instructions_from_file('input.txt') # use input.txt/input_test.txt
start_position = 50
final_position, zero_counter, zero_crossings_counter = run_instructions(instructions, start_position)

print(f"Final Position: {final_position}")
print(f"Number of times position 0 was reached: {zero_counter}")
print(f"Number of zero crossings: {zero_crossings_counter}")

