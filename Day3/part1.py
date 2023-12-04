import sys

SYMBOLS = {'@', '#', '$', '%', '&', '*', '-', '=', '+', '/'}

with open(sys.argv[1]) as f:
    DATA = [list(line) for line in f]
    row_len = len(DATA)
    col_len = len(DATA[0])

def check(row, col):
    if row < 0 or row >= len(DATA):
        return False
    
    if col - 1 > 0 and DATA[row][col - 1] in SYMBOLS or DATA[row][col] in SYMBOLS or col + 1 < len(DATA[0]) and DATA[row][col + 1] in SYMBOLS:
        return True

    return False

def gear_ratios():
    sum = 0
    for row in range(len(DATA)):
        adjacent = False
        curr_part = ''
        for col in range(len(DATA[row])):
            if DATA[row][col].isnumeric():
                curr_part += DATA[row][col]
                if not adjacent:
                    if check(row - 1, col) or check(row + 1, col) or check(row, col):
                        adjacent = True
            elif curr_part:
                if adjacent:
                    sum += int(curr_part)
                curr_part = ''
                adjacent = False
        if curr_part and adjacent:
            sum += int(curr_part)
    return sum

print(gear_ratios())