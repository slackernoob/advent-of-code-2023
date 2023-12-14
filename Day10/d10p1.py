import sys

# data = [[char for char in line.strip()] for line in sys.stdin]
data = []
row = 0
start = None
for line in sys.stdin:
    line = line.rstrip()
    r = []
    for i in range(len(line)):
        if line[i] == "S":
            start = (row, i)
        r.append(line[i])
    data.append(r)
    row += 1



def get_initial_neighbours(start, data):
    moves = [[-1,0], [1,0], [0,-1], [0,1]] # up, down, left, right movements
    neighbours = []
    for i in range(4):
        new_i = start[0] + moves[i][0]
        new_j = start[1] + moves[i][1]
        if i == 0:
            if data[new_i][new_j] in ["|", "7", "F"]:
                neighbours.append((new_i, new_j))
        elif i == 1:
            if data[new_i][new_j] in ["|", "L", "J"]:
                neighbours.append((new_i, new_j))
        elif i == 2:
            if data[new_i][new_j] in ["-", "L", "F"]:
                neighbours.append((new_i, new_j))
        else:
            if data[new_i][new_j] in ["-", "7", "J"]:
                neighbours.append((new_i, new_j))
    return neighbours

pipe_mappings = {"|": [(-1, 0), (1, 0)],
                 "-": [(0, -1), (0, 1)],
                 "L": [(-1, 0), (0, 1)],
                 "J": [(-1, 0), (0, -1)],
                 "7": [(0, -1), (1, 0)],
                 "F": [(0, 1), (1, 0)],
                }
cur = get_initial_neighbours(start, data)
next_neighbours = []
dist = 1
visited = [start]
while True:
    for coord in cur:
        visited.append(coord)
        pipe = data[coord[0]][coord[1]]
        movements = pipe_mappings[pipe]
        for movement in movements:
            new_i = coord[0] + movement[0]
            new_j = coord[1] + movement[1]
            if (new_i, new_j) not in visited:
                next_neighbours.append((new_i, new_j))
    cur = next_neighbours
    next_neighbours = []
    dist += 1
    # print(cur)
    if len(set(cur)) == 1:
        break
    
print(dist)

# visited = []

# found = False
# dist = 0
# while not found:
#     while S:
#         cur = S.pop()
#         visited.append(cur)
#         for i in range(4):
#             new_r = cur[0] + moves[i][0]
#             new_c = cur[1] + moves[i][1]
#             if data[new_r][new_c] in allowed_pipes[moves[i]]:
#                 if (new_r, new_c) in S:
#                     break
#                 else:
#                     S.add((new_r, new_c))
#     dist += 1

# print(dist)
        
