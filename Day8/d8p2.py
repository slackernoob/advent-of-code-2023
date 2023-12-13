import sys, math

instructions = input()
input()
print(instructions)

hashmap = {}
cur_list = []
for line in sys.stdin:
    line = line.strip()
    key = line[:3]
    if key[-1] == "A":
        cur_list.append(key)
    value = (line[7:10], line[12:15])
    hashmap[key] = value

step_list = []
for cur in cur_list:
    steps = 0
    isFound = False
    while not isFound:
        for letter in instructions:
            if letter == "R":
                cur = hashmap[cur][1]
            else:
                cur = hashmap[cur][0]
            steps += 1
            if cur[-1] == "Z":
                isFound = True
                step_list.append(steps)
                break
print(math.lcm(*step_list))