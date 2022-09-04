q = input()
n = 0
for i in range(8):
    r = input().split()
    if "1" in r:
        n += 1

print(n)