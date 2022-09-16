n = int(input())
a = [int(i) for i in input().split()]
total = sum(a)

ans = -1
left = 0
for i in range(n):
    left += a[i]
    right = total - left
    if left == right:
        ans = i + 1
        break
print(ans)