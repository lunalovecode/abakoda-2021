a = input().split()
abby_times = [int(a[0]), int(a[1])]
cody_times = [int(a[2]), int(a[3])]

if (abby_times[1] <= cody_times[0]) or (cody_times[1] <= abby_times[0]):
    print("NO")
else:
    print("YES")