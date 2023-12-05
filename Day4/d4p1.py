import sys

total = 0
for line in sys.stdin:
    line = line.rstrip()
    data = line.split(": ")
    all_numbers = data[1].split(" | ")
    winning_numbers = [int(num.strip()) for num in filter(lambda x: len(x)!=0, all_numbers[0].split(" "))]
    my_numbers = [int(num.strip()) for num in filter(lambda x: len(x)!=0, all_numbers[1].split(" "))]
    num_winning = 0
    
    for num in my_numbers:
        if num in winning_numbers:
            num_winning += 1

    if num_winning != 0:
        points = 1
        for _ in range(num_winning-1):
            points *= 2
        total += points
print(total)