import math
import sys

with open(sys.argv[1]) as file:
    DATA = [line.strip() for line in file if line.strip()]

instructions_line = DATA[0]

maps = {}

def lcm_array(arr):
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    result = arr[0]
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])
    
    return result

def find_steps():
    for i in range(1, len(DATA)):
        key, value = DATA[i].split('=')
        maps.update({key.strip() : value[2:-1].split(', ')})

    starters = []
    for key in maps.keys():
        if key[-1] == 'A':
            starters.append(key)

    multiples = [0] * len(starters)
    steps = 0
    instructions = list(instructions_line)
    while multiples.count(0) != 0:
        for instruction in instructions:
            for i in range(len(starters)):
                current = starters[i]
                if instruction == 'L':
                    starters[i] = maps.get(current)[0]
                else:
                    starters[i] = maps.get(current)[1]
            steps +=1

        for i in range(len(starters)):
            if starters[i][-1] == 'Z':
                multiples[i] = steps
    
    return lcm_array(multiples)

print(find_steps())