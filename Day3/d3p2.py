import functools
import sys

data = [[c for c in line.rstrip()] for line in sys.stdin]
rows = len(data)
cols = len(data[0])
total = 0

def getNumbers(row_data):
    nums = []
    i = 0
    while i < len(row_data):
        if row_data[i].isdigit():
            start_index = i
            numString = ""
            while i < len(row_data) and row_data[i].isdigit():
                numString += row_data[i]
                i += 1
            end_index = i - 1
            nums.append([numString, (start_index, end_index)])
        else:
            i += 1
    return nums

def getSymbols(row_data):
    symbols = []
    for i in range(len(row_data)):
        if row_data[i] == "*":
            symbols.append(i)
    return symbols

for i in range(rows):
    symbols = getSymbols(data[i])
    if i == 0:
        next_row = getNumbers(data[i+1])
        for symbol in symbols:
            gears = []
            for num in next_row:
                left = max(num[1][0] - 1, 0)
                right = min(num[1][1] + 1, cols)
                if left <= symbol <= right:
                    value = int(num[0])
                    gears.append(value)
            # Check left of gear
            pointer = symbol - 1
            numString = ""
            while pointer >= 0 and data[i][pointer].isdigit():
                numString = data[i][pointer] + numString
                pointer -= 1
            if len(numString) > 0:
                gears.append(int(numString))
            # Check right of gear
            pointer = symbol + 1
            numString = ""
            while pointer < cols and data[i][pointer].isdigit():
                numString = numString + data[i][pointer]
                pointer += 1
            if len(numString) > 0:
                print(numString)
                gears.append(int(numString))
            if len(gears) == 2:
                total += functools.reduce(lambda x,y: x*y, gears)
    elif i == rows - 1:
        prev_row = getNumbers(data[i-1])
        for symbol in symbols:
            gears = []
            for num in prev_row:
                left = max(num[1][0] - 1, 0)
                right = min(num[1][1] + 1, cols)
                if left <= symbol <= right:
                    value = int(num[0])
                    gears.append(value)
            # Check left of gear
            pointer = symbol - 1
            numString = ""
            while pointer >= 0 and data[i][pointer].isdigit():
                numString = data[i][pointer] + numString
                pointer -= 1
            if len(numString) > 0:
                gears.append(int(numString))
            # Check right of gear
            pointer = symbol + 1
            numString = ""
            while pointer < cols and data[i][pointer].isdigit():
                numString = numString + data[i][pointer]
                pointer += 1
            if len(numString) > 0:
                print(numString)
                gears.append(int(numString))
            if len(gears) == 2:
                total += functools.reduce(lambda x,y: x*y, gears)
    else:
        next_row = getNumbers(data[i+1])
        prev_row = getNumbers(data[i-1])
        combined_row = next_row + prev_row
        for symbol in symbols:
            gears = []
            for num in combined_row:
                left = max(num[1][0] - 1, 0)
                right = min(num[1][1] + 1, cols)
                if left <= symbol <= right:
                    value = int(num[0])
                    gears.append(value)
            # Check left of gear
            pointer = symbol - 1
            numString = ""
            while pointer >= 0 and data[i][pointer].isdigit():
                numString = data[i][pointer] + numString
                pointer -= 1
            if len(numString) > 0:
                gears.append(int(numString))
            # Check right of gear
            pointer = symbol + 1
            numString = ""
            while pointer < cols and data[i][pointer].isdigit():
                numString = numString + data[i][pointer]
                pointer += 1
            if len(numString) > 0:
                gears.append(int(numString))
            if len(gears) == 2:
                total += functools.reduce(lambda x,y: x*y, gears)
print(total)
