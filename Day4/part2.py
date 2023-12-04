import re
import sys

with open(sys.argv[1]) as lines:
    DATA = [line for line in lines]

def add_copies(copies, current, count):
    for i in range(current, current + count):
        copies.append(DATA[i][:-1])

def scratchcards():
    sum = len(DATA)
    winnings = {}
    for line in DATA:
        copies = []
        card_id, cards = line.split(':')
        id = int(re.findall(r'\d+', card_id)[0])
        winner, hand = cards.strip().split('|')
        counter = 0
        if id in winnings:
            counter = winnings.get(id)
        else:
            for i in hand.strip().split(' '):
                if i == '' or i == ' ':
                    continue
                if i in winner.strip().split(' '):
                    counter += 1
            winnings.update({id : counter})
        if counter > 0:
            add_copies(copies, id, counter)
            sum += counter

        while True:
            if len(copies) == 0:
                break
            current_scratch = copies.pop()
            current_scratch_id, current_cards = current_scratch.split(':')
            current_id = int(re.findall(r'\d+', current_scratch_id)[0])
            current_winner, current_hand = current_cards.strip().split('|')
            current_counter = 0
            if current_id in winnings:
                current_counter = winnings.get(current_id)
            else:
                for i in current_hand.strip().split(' '):
                    if i == '' or i == ' ':
                        continue
                    if i in current_winner.strip().split(' '):
                        current_counter += 1
                winnings.update({current_id : current_counter})

            if current_counter > 0:
                add_copies(copies, current_id, current_counter)
                sum += current_counter

    return sum

print(scratchcards())
