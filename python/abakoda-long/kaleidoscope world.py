def distance(x1, y1, x2, y2):
    col, row = abs(x1 - x2), abs(y1 - y2)
    return int(col + max(0, (row - col) / 2))
dic = {}
for i in range(int(input())):
    name, x, y = input(), 0, 0
    for i in range(int(input())):
        t, k = input().split()
        if t == 'U':
            y += 2 * int(k)
        elif t == 'D':
            y -= 2 * int(k)
        elif t == 'LU':
            x, y = x - int(k), y + int(k)
        elif t == 'LD':
            x, y = x - int(k), y - int(k)
        elif t == 'RU':
            x, y = x + int(k), y + int(k)
        elif t == 'RD':
            x, y = x + int(k), y - int(k)
    dic[name] = [x, y]
for i in range(int(input())):
    name1, name2 = input().split()
    print(distance(dic[name1][0], dic[name1][1], dic[name2][0], dic[name2][1]))