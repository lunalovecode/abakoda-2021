b = int(input())

library_filled = [False for i in range(1141)]

for i in range(b):
    enter, exit = [int(x) for x in input().split()]
    for time in range(enter, exit):
        library_filled[time] = True

free_time = 0

for time in range(420, 1140):
    if not library_filled[time]:
        free_time += 1

print(free_time)