n = int(input())
grid= input()
ans = [[-1] * n for i in range(2)]
final = []
for i in range(n):
    if grid[i] == 'A':
        final.append((i,0))
        ans[0][i] = 0
    if grid[i] == 'C':
        final.append((i,1))
        ans[1][i] = 0
z = 0
while z < len(final):
    p,c = final[z]
    for x in [-1,1]:
        if 0 <= p + x and p + x < n and grid[p + x] == '.' and ans[c][p + x] == -1:
            ans[c][p + x] = ans[c][p] + 1
            final.append((p + x,c))
    z += 1
print(*ans[0])
print(*ans[1])