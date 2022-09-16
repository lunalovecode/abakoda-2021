d = int(input())
height = [int(i) for i in input().split()]

ans = d - 1

group_size = {}

# dhelmise is a pokemon that looks like an anchor
for dhelmise in range(d):
    smallest_height = height[dhelmise] - dhelmise
    if smallest_height not in group_size:
        group_size[smallest_height] = 0
    group_size[smallest_height] += 1

ans = d - 1

for group, size in group_size.items():
    ans = min(ans, d - size)
print(ans)