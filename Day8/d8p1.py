import sys

instructions = input()
input()
print(instructions)

hashmap = {}
for line in sys.stdin:
    line = line.strip()
    key = line[:3]
    value = (line[7:10], line[12:15])
    hashmap[key] = value
print(hashmap)

cur = "AAA"
steps = 0
isFound = False
while not isFound:
    for letter in instructions:
        if letter == "R":
            cur = hashmap[cur][1]
        else:
            cur = hashmap[cur][0]
        steps += 1
        if cur == "ZZZ":
            isFound = True
            break
print(steps)
