import sys
from functools import cmp_to_key, reduce

card_rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
             '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11,
             'Q': 12, 'K': 13, 'A': 14}

data = [line.strip().split(" ") for line in sys.stdin]

def changeToInt(data):
    data[1] = int(data[1])
    return data
data = list(map(changeToInt, data))


def getType(hand):
    cards = {}
    for card in hand:
        if cards.get(card, None) == None:
            cards[card] = 1
        else:
            cards[card] = cards.get(card) + 1
    if len(cards.keys()) == 1:
        return 6
    if 4 in cards.values() and 1 in cards.values():
        return 5
    if 3 in cards.values() and 2 in cards.values():
        return 4
    if 3 in cards.values() and 1 in cards.values():
        return 3
    if 2 in cards.values() and 1 in cards.values() and len(cards.values()) == 3:
        return 2
    if 2 in cards.values() and len(cards.values()) == 4:
        return 1
    return 0

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
