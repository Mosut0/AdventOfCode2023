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

print(points(sys.argv[1]))
