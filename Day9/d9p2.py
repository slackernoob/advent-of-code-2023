import sys

data = [[list(map(lambda x: int(x), line.strip().split(" ")))] for line in sys.stdin]

total = 0
for history in data:
    cur = history[0]
    while len(set(cur)) != 1:
        cur = [cur[i] - cur[i-1] for i in range(1, len(cur))]
        history.append(cur)
    cur = 0
    for i in range(len(history)-1, -1, -1):
        cur = history[i][0] - cur
    total += cur
    
print(total)
