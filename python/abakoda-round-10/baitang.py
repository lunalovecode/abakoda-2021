n = int(input())
height = [int(i) for i in input().split()]

if max(height) - min(height) in [n, n - 1]:
    print("Yes")
    for i in range(min(height) + 1, max(height)):
        if i not in height:
            print(i)
else:
    print("No")