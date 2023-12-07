import math
import re
import sys

with open(sys.argv[1]) as f:
    DATA = f.read()

def winner_product():
    str_time = [num for num in re.search(r'Time:([\s\d]+)', DATA).group(1).split()]
    str_distance = [num for num in re.search(r'Distance:([\s\d]+)', DATA).group(1).split()]
    time = int(''.join(str_time))
    distance = int(''.join(str_distance))
    det = math.sqrt(time ** 2 - 4 * distance)
    return math.ceil((time + det) / 2) - math.floor((time - det) / 2) - 1

print(winner_product())
