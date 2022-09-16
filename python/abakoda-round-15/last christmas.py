friends = int(input())
pieces = int(input())

ans = "IMPOSSIBLE"

for i in range(1, friends):
    if (i * pieces) % friends == 1 and (i * pieces) % friends < 1000:
        ans = i

print(ans)