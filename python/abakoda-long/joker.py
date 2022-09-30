n, m = [int(x) for x in input().split()]
cards = list(input())
jokers = cards.count("*")
vals = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10, "*": 0}
total = sum(vals[i] for i in cards if i != '*')
if total+jokers <= m <= total+jokers*10:
    print("YES")
    m -= total+jokers
    for i in range(n):
        if cards[i] == '*': cards[i] = 1
    for i in range(n):
        if type(cards[i]) == int:
            cards[i] = '.A23456789T'[1+min(9,m)]
            m = max(0,m-9)
    print(''.join(cards))
else:
    print("NO")