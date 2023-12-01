import sys


total = 0
for line in sys.stdin:
    line = line.rstrip()
    first = None
    last = None
    length = len(line)

    for x in range(length):
        if line[x].isdigit():
            first = line[x]
            break
    
    for x in range(length-1, -1, -1):
        if line[x].isdigit():
            last = line[x]
            break
    num = int(first + last)
    total += num

print(total)