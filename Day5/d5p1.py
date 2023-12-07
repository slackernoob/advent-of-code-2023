line = input().rstrip()[7:]
input() # Get rid of blank line below seeds
seeds = [int(x) for x in line.split(" ")]

mapping_data = [[] for x in range(7)]

n = -1
while True:
    try:
        line = input().rstrip()
        if len(line) == 0:
            continue
        elif not line[0].isdigit():
            n += 1
        else:
            values = list(map(lambda x: int(x), line.split(" ")))
            mapping_data[n].append(values)
    except EOFError:
        break

lowest = 100000000000000
for seed in seeds:
    cur = seed
    for mappings in mapping_data:
        for mapping in mappings:
            if mapping[1] <= cur <= mapping[1] + mapping[2]:
                cur += mapping[0] - mapping[1]
                break
    if cur < lowest:
        lowest = cur

print(lowest)