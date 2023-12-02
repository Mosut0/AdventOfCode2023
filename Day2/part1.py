import re
import sys

BAG = {
    "blue" : 14,
    "green" : 13,
    "red" : 12
}

def valid_draw(file):
    sum = 0
    with open(file) as input:
        for line in input:
            game_draws = line.split(":")
            game_Id = game_draws[0].split(" ")[1]
            flag = True
            for draw in game_draws[1].split(";"):
                if flag:
                    for colours in draw.split(','):
                        amount, colour = colours.strip().split(" ")
                        if int(amount) > BAG.get(colour):
                            flag = False
                            break
                else:
                    break
            if flag:
                sum += int(game_Id)
    return sum

print(valid_draw(sys.argv[1]))
