# Time:      7  15   30
# Distance:  9  40  200

import sys

data = [line.strip() for line in sys.stdin]

duration = int(data[0][7:].replace(" ", ""))
record = int(data[1][9:].replace(" ", ""))
smallest_num = 0
for x in range(1, duration):
    dist = x * (duration - x)
    if dist > record:
        smallest_num = x
        break
biggest_num = duration - smallest_num
num_ways_to_win = biggest_num - smallest_num + 1
print(num_ways_to_win)