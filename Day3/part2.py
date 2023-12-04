import sys

SYMBOL = '*'

gear_parts = {}
curr_pair = ()

with open(sys.argv[1]) as f:
    DATA = [list(line) for line in f]
    row_len = len(DATA)
    col_len = len(DATA[0])

def check(row, col):
    global curr_pair
    if row < 0 or row >= len(DATA):
        return False
    
    if col - 1 > 0 and DATA[row][col - 1] == SYMBOL:
        curr_pair = (row, col - 1)
        gear_parts.setdefault(curr_pair, [])
        return True
    elif DATA[row][col] == SYMBOL:
        curr_pair = (row, col)
        gear_parts.setdefault(curr_pair, [])
        return True
    elif col + 1 < len(DATA[0]) and DATA[row][col + 1] == SYMBOL:
        curr_pair = (row, col + 1)
        gear_parts.setdefault(curr_pair, [])
        return True

    return False

def gear_ratios():
    global curr_pair
    sum = 0
    for row in range(len(DATA)):
        adjacent = False
        curr_part = ''
        curr_pair = ()
        for col in range(len(DATA[row])):
            if DATA[row][col].isnumeric():
                curr_part += DATA[row][col]
                if not adjacent:
                    if check(row - 1, col) or check(row + 1, col) or check(row, col):
                        adjacent = True
            elif curr_part:
                if adjacent:
                    arr = gear_parts.get(curr_pair)
                    arr.append(int(curr_part))
                    gear_parts.update({curr_pair : arr})
                curr_pair = ()
                curr_part = ''
                adjacent = False
        if curr_part and adjacent:
            arr = gear_parts.get(curr_pair)
            arr.append(int(curr_part))
            gear_parts.update({curr_pair : arr})

    for gear in gear_parts.values():
        if len(gear) == 2:
            sum += gear[0] * gear[1]

    return sum 
        

print(gear_ratios())