import sys


mapping = {'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8', 
        'nine': '9',
        }
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
r_nums = [x[::-1] for x in nums]

def indexing(s, vals):
    length = len(s)
    threshold = length
    for a in range(length):
        if s[a].isdigit():
            threshold = a
            break
    i = length 
    val = None
    for word in vals:
        try:
            x = s.index(word)
            # print(x, word)
            if x < i and x<threshold:
                i = x
                val = word
        except:
            pass
    return (i, val)

total = 0
for line in sys.stdin:
    line = line.rstrip()

    first = None
    last = None
    
    front = indexing(line, nums)
    if front[1] != None:
        line = line.replace(front[1], mapping[front[1]], 1)
    
    r_line = line[::-1]

    back = indexing(r_line, r_nums)
    if back[1] != None:
        line = r_line.replace(back[1], mapping[back[1][::-1]], 1)[::-1]

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