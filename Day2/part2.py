import re
import sys

from functools import reduce

def min_draw(file):
    sum = 0
    with open(file) as input:
        for line in input:
            min_amount = {
                "blue" : 0,
                "green" : 0,
                "red" : 0
            }
            game_draws = line.split(":")[1].strip()
            matches = re.findall(r'(\d+)\s+(\w+)', game_draws)
            for amount, colour in matches:
                min_amount.update({colour : max(min_amount.get(colour), int(amount))})
            sum += reduce(lambda x, y: x * y, min_amount.values())
    return sum

print(min_draw(sys.argv[1]))
