import sys
from functools import cmp_to_key, reduce

card_rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
             '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1,
             'Q': 12, 'K': 13, 'A': 14}

data = [line.strip().split(" ") for line in sys.stdin]

def changeToInt(data):
    data[1] = int(data[1])
    return data
data = list(map(changeToInt, data))


def getType(hand):
    cards = {}
    num_j = 0
    type = 0 # high card
    for card in hand:
        if card == "J":
            num_j += 1
        elif cards.get(card, None) == None:
            cards[card] = 1
        else:
            cards[card] = cards.get(card) + 1
    if 5 in cards.values():
        type = 6 # five of a kind
        return type
    elif 4 in cards.values():
        type = 5 # four of a kind
        return type + num_j
    elif 3 in cards.values() and 2 in cards.values():
        type = 4 # full house
        return type + num_j
    elif 3 in cards.values():
        type = 3 # three of a kind
        if num_j == 1:
            type = 5
        elif num_j == 2:
            type = 6
        return type
    elif 2 in cards.values() and list(cards.values()).count(2) == 2:
        type = 2 # two pair
        if num_j == 1:
            return 4
        elif num_j == 2:
            return 5
        else:
            return type
    if 2 in cards.values() and list(cards.values()).count(2) == 1:
        type = 1 # one pair
        if num_j == 1:
            type = 3
        elif num_j == 2:
            type = 5
        elif num_j == 3:
            type = 6
        return type
    j_type = [0, 1, 3, 5, 6, 6]
    return j_type[num_j] 

def comparator(a, b):
    a_hand = a[0]
    b_hand = b[0]
    a_type = getType(a_hand)
    b_type = getType(b_hand)
    if a_type > b_type:
        return 1
    elif a_type < b_type:
        return -1
    else:
        for i in range(5):
            if card_rank[a_hand[i]] > card_rank[b_hand[i]]:
                return 1
            elif card_rank[a_hand[i]] < card_rank[b_hand[i]]:
                return -1
            else:
                continue
        return 0

data = sorted(data, key=cmp_to_key(comparator))
ans = 0
for i in range(len(data)):
    ans += (i+1) * data[i][1]
print(ans)
