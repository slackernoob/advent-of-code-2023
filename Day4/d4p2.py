import sys

cards = {}
total = 0
for line in sys.stdin:
    line = line.rstrip()
    data = line.split(": ")
    card_no = int(data[0][4:].strip())

    if card_no not in cards.keys():
        cards[card_no] = 1
    else:
        cards[card_no] = cards[card_no] + 1
    all_numbers = data[1].split(" | ")
    winning_numbers = [int(num.strip()) for num in filter(lambda x: len(x)!=0, all_numbers[0].split(" "))]
    my_numbers = [int(num.strip()) for num in filter(lambda x: len(x)!=0, all_numbers[1].split(" "))]
    num_winning = 0

    for num in my_numbers:
        if num in winning_numbers:
            num_winning += 1

    for num in range(card_no + 1, card_no + 1 + num_winning):
        if num not in cards.keys():
            cards[num] = cards[card_no]
        else:
            cards[num] = cards[num] + cards[card_no]

    total += cards[card_no]
print(total)