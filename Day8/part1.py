import sys

with open(sys.argv[1]) as file:
    DATA = [line.strip() for line in file if line.strip()]

instructions_line = DATA[0]
maps = {}

def find_steps():
    for i in range(1, len(DATA)):
        key, value = DATA[i].split('=')
        maps.update({key.strip() : value.split()})

    current = 'AAA'
    steps = 0
    instructions = list(instructions_line)
    while current != 'ZZZ':
        for instruction in instructions:
            if instruction == 'L':
                current = maps.get(current)[0][1:-1]
            else:
                current = maps.get(current)[1][:-1]
            steps += 1

    return steps

print(find_steps())