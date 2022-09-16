from bisect import *
n, L = [int(i) for i in input().split()]
lst = [int(i) for i in input().split()]
lst.sort()

all_pairs = []
for i in range(n):
    for j in range(i + 1, n):
        all_pairs.append(lst[i] + lst[j])
all_pairs.sort()

def count_in_range(lst, val, l, r):
    return bisect(lst, val, l, r)

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        a = lst[i] + lst[j]
        ans += bisect(all_pairs, L - (lst[i] + lst[j]))
print(ans)
