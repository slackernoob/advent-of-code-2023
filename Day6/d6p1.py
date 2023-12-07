# Time:      7  15   30
# Distance:  9  40  200

import sys

data = [line.strip() for line in sys.stdin]

times = [int(timing) for timing in filter(lambda x: len(x)!=0, data[0][7:].strip().split(" "))]
distances = [int(timing) for timing in filter(lambda x: len(x)!=0, data[1][9:].strip().split(" "))]

num_races = len(times)

margin_of_error = 1
for n in range(num_races):
    duration = times[n]
    record = distances[n]
    min_hold = 0
    for x in range(1, duration):
        dist = x * (duration - x)
        if dist > record:
            min_hold = x
            break
    max_hold = duration - min_hold
    num_ways_to_win = max_hold - min_hold + 1
    margin_of_error *= num_ways_to_win

print(margin_of_error)
