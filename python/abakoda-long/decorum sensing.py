n =  int(input())
priorities = [int(x) for x in input().split()]
priorities.sort()

count = 0
for i in range(n):
    if count >= priorities[i]:
        count += 1
print(count)