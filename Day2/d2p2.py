import sys



total = 0
for line in sys.stdin:
    thresholds = {"green": 0,
              "red": 0,
              "blue": 0,
              }
    line = line.rstrip()
    line = line.split(": ")
    id = int(line[0][5:])
    
    isPossible = True
    subsets = line[1].split("; ")
    print(subsets)
    for subset in subsets:
        colours = subset.split(", ")
        for color in colours:
            breakdown = color.split(" ")
            name = breakdown[1]
            value = int(breakdown[0])
            if value > thresholds[name]:
                thresholds[name] = value
    power = 1
    for k in thresholds.values():
        power *= k
    total += power


print(total)