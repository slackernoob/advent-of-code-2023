line = input().rstrip()[7:]
input() # Get rid of blank line below seeds
seeds = [int(x) for x in line.split(" ")]

seed_bible = {1: {},
              2: {},
              3: {},
              4: {},
              5: {},
              6: {},
              7: {}}

n = 0
while True:
    try:
        line = input().rstrip()
        if len(line) == 0:
            continue
        elif not line[0].isdigit():
            n += 1
        else:
            values = list(map(lambda x: int(x), line.split(" ")))
            des_start = values[0]
            src_start = values[1]
            range_length = values[2]
            for r in range(range_length):
                des = des_start + r
                src = src_start + r
                if src not in seed_bible[n].keys():
                    seed_bible[n][src] = des
    except EOFError:
        break

locations = []
for seed in seeds:
    cur = seed
    for b in range(1, 8):
        if cur in seed_bible[b].keys():
            cur = seed_bible[b][cur]
    locations.append(cur)

print(locations)
print(min(locations))