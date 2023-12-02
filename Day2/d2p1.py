import sys

thresholds = {"green": 13,
              "red": 12,
              "blue": 14,
              }

total = 0
for line in sys.stdin:
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
                isPossible = False
                break
        if isPossible == False:
            break
    
    if isPossible == True:
        total += id


print(total)