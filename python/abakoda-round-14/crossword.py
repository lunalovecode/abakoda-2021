from itertools import permutations
r, c = map(int, input().split())
grid = []
for i in range(r):
    grid.append(list(input()))
across = set()
ac = int(input())
for i in range(ac):
    across.add(input())
down = []
dwn = int(input())
for i in range(dwn):
    down.append(input())
dwncoords = []
for x in range(c):
    curr = []
    for y in range(r):
        if grid[y][x] == "_":
            curr.append([y, x])
        elif curr:
            curr.append(len(curr))
            dwncoords.append(curr)
            curr = []
    if curr:
        curr.append(len(curr))
        dwncoords.append(curr)
        curr = []
for a in permutations(down):
    flag = False
    for i in range(dwn):
        if len(a[i]) == dwncoords[i][-1]:
            for dex, letter in enumerate(a[i]):
                grid[dwncoords[i][dex][0]][dwncoords[i][dex][1]] = letter
        else:
            flag = True
            break
    if flag:
        continue
    for ro in grid:
        curr = []
        for letter in ro:
            if letter != "*":
                curr.append(letter)
            elif curr:
                s = "".join(curr)
                if s in across:
                    curr = []
                else:
                    flag = True
                    break
        if curr:
            s = "".join(curr)
            if s in across:
                curr = []
            else:
                flag = True
                break
        if flag:
            break
    if flag:
        continue
    else:
        for line in grid:
            print("".join(line))
        break