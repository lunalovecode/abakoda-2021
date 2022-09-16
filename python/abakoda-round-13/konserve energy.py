c = int(input())
events = []
entered = [0 for i in range(68401)]
exited = [0 for i in range(68401)]

for i in range(c):
    enter, exit = [int(x) for x in input().split()]
    entered[enter] += 1
    exited[exit] += 1

events.sort()
ans = 0
people_in_library = 0
for time in range(25200, 68400):
    if people_in_library == 0:
        ans += 1
    people_in_library += entered[time]
    people_in_library -= exited[time]

print(ans)