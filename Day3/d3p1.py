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

for i in range(rows):
    info = getNumbers(data[i])
    for item in info:
        k = item[0]
        v = item[1]
        isPartNumber = False
        for r in range(i-1, i+2):
            if isPartNumber:
                break
            if r >= 0 and r < rows:
                if r == i:
                    # check to left and right of number in same row
                    left = v[0] - 1
                    right = v[1] + 1
                    if left >= 0 and left < cols:
                        if not data[r][left].isdigit() and data[r][left] != ".":
                            isPartNumber = True
                            break
                    if right >= 0 and right < cols:
                        if not data[r][right].isdigit() and data[r][right] != ".":
                            isPartNumber = True
                            break
                else:
                    for c in range(v[0]-1, v[1]+2):
                        if c >= 0 and c < cols:
                            if not data[r][c].isdigit() and data[r][c] != ".":
                                isPartNumber = True
                                break
        if isPartNumber:
            total += int(k)
print(total)