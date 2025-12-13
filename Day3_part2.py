# Now, you need to make the largest joltage by turning on EXACTLY twelve
# batteries within each bank.

# The joltage output for the bank is still the number formed by the digits
# of the batteries you've turned on; the only difference is that now there
# will be 12 digits in each bank's joltage output instead of two.

# https://ideone.com/zDPvjc

def read_banks_from_file(filename):
    with open(filename, 'r') as file:
        ban = [line.strip() for line in file.readlines()]
    return ban

banks = read_banks_from_file('input_day3_test.txt')

def largest_after_removing_k(s: str, k: int) -> str:

    stack = []

    print(s)
    for ch in s.strip():
        while len(stack) > 0 and k > 0 and ch > stack[-1]:
            stack.pop() # default pos = -1, delete last element
            k -= 1
        stack.append(ch) # add ch to the list.
        print(stack)

    if k > 0:
        stack = stack[:-k]

    return "".join(stack)

def largest_with_exactly_12_digits(s: str) -> str:
    digits = [ch for ch in s if ch.isdigit()]
    k = max(0, len(digits) - 12)
    return largest_after_removing_k("".join(digits), k)[:12]

all_joltages = []
for t in banks:
    all_joltages.append(largest_with_exactly_12_digits(t))

result = sum(int(joltage) for joltage in all_joltages)
print(result)
