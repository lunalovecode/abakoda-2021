from bisect import *

c = int(input())
lst = [int(i) for i in input().split()]
lst.sort()

ans = 0
for i in range(c):
    for j in range(i + 1, c):
        n = lst[i] + lst[j]
        
        t = bisect_left(lst, n, j + 1, c) - 1
        ans += t - j

print(ans)