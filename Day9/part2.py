import sys

with open(sys.argv[1]) as file:
    DATA = [line.strip() for line in file if line.strip()]

def mirage_maintenance():
    ans = 0
    def find_history(data):
        history = []
        data = [int(num) for num in data]
        data.reverse()
        history.append(data)
        while not all(element == 0 for element in history[-1]):
            current = history[-1]
            temp = []
            for i in range(1, len(current), 1):
                temp.append(current[i] - current[i-1])
            history.append(temp)
        history[-1].append(0)
        for i in range(len(history) - 1, 0, -1):
            history[i-1].append(history[i-1][-1] + history[i][-1])
        return history[0][-1]

    for data in DATA:
        ans += find_history(data.split(' '))
    
    return ans

print(mirage_maintenance())
