import sys

def points(file):
    with open(file) as lines:
        sum = 0
        for line in lines:
            cards = line.split(':')[1].strip()
            winner, hand = cards.split('|')
            temp = 0
            counter = 1
            for i in hand.strip().split(' '):
                if i == ' ' or i == '':
                    continue
                if i in winner.strip().split(' '):
                    if counter > 1:
                        temp *= 2
                    else:
                        temp = 1
                    counter += 1
            sum += temp
            temp = 0
    
    return sum

# Alternative, cleaner + better solution
def solution(lines: list[str]) -> int:
    total = 0

    for line in lines:
        line = line[line.find(':') + 2:].split(' | ')
        winning_nums = {n for n in line[0].split()}
        nums = {n for n in line[1].split()}

        diff = len(winning_nums) - len(winning_nums - nums)
        if diff > 0:
            total += 2 ** (diff - 1)
    return total

print(points(sys.argv[1]))
