r, c = map(int, input().split())
d = {}
grid = [input() for i in range(r)]
 
def solve(x, y, d):
    while x >= 0 and x < c and y >= 0 and y < r:
        if grid[y][x] == "/":
            d = [-d[1], -d[0]]
        else:
            d = [d[1], d[0]]
        x += d[0]
        y += d[1]
    if x < 0:
        return "L " + str(y + 1)
    elif x == c:
        return "R " + str(y + 1)
    elif y < 0:
        return "T " + str(x + 1)
    else:
        return "B " + str(x + 1)
 
for i in range(r):
    k = "L " + str(i + 1)
    if k not in d:
        h = solve(0, i, [1, 0])
        d[h] = k
        d[k] = h
    k = "R " + str(i + 1)
    if k not in d:
        h = solve(c - 1, i, [-1, 0])
        d[h] = k
        d[k] = h
 
for i in range(c):
    k = "T " + str(i + 1)
    if k not in d:
        h = solve(i, 0, [0, 1])
        d[h] = k
        d[k] = h
    k = "B " + str(i + 1)
    if k not in d:
        h = solve(i, r - 1, [0, -1])
        d[h] = k
        d[k] = h
 
x = []
for i in range(int(input())):
    x.append(d[input()])
print("\n".join(x))