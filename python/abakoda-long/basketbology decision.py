n = int(input())
baskets = [int(x) for x in input().split()]
skill_levels = [int(x) for x in input().split()]
ans = []
baskets.sort()
skill_levels.sort()

for i in range(n):
    if skill_levels[i] >= baskets[i]:
        ans.append(True)
    else:
        ans.append(False)

if all(ans):
    print("YES")
else:
    print("NO")
