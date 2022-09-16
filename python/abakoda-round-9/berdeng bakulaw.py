b = input().split()
n = int(b[0])
m = int(b[1])
times_paired = []
for i in range(n):
    times_paired.append(0)

for j in range(m):
    r = input().split()
    times_paired[int(r[0]) - 1] = times_paired[int(r[0]) - 1] + 1
    times_paired[int(r[1]) - 1] = times_paired[int(r[1]) - 1] + 1

def func(k):
    return str(k)

new_times_paired = map(func, times_paired)
print(" ".join(new_times_paired))