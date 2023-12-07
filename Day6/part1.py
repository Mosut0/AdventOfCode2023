import math
import re
import sys

with open(sys.argv[1]) as f:
    DATA = f.read()

def winner_product():
    time = [int(num) for num in re.search(r'Time:([\s\d]+)', DATA).group(1).split()]
    distance = [int(num) for num in re.search(r'Distance:([\s\d]+)', DATA).group(1).split()]
    ans = 1
    for race in range(len(time)):
        det = math.sqrt(time[race] ** 2 - 4 * distance[race])
        ans *= (math.ceil((time[race] + det) / 2) - math.floor((time[race]- det) / 2) - 1)
    return ans

print(winner_product())
