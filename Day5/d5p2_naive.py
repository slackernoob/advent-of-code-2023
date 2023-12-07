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

score = 0
seeds2 = [(seeds[2*n], seeds[2*n+1]) for n in range(len(seeds)//2)]
print(seeds2)

toContinue = True
while True:
    print(score)
    cur = score
    for mappings in mapping_data[::-1]:
        for mapping in mappings:
            d, s, r = mapping[0], mapping[1], mapping[2]
            if d <= cur <= d + r - 1:
                cur += s - d
                break
    for i, j in seeds2:
        if i <= cur <= i + j - 1:
            print(score)
            toContinue = False
            break
    score += 1
    if toContinue == False:
        break