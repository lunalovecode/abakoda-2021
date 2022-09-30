from math import gcd
t = int(input())
for i in range(t):
    w, h, x, y = [int(x) for x in input().split()]
    a = h * x // gcd(h * x, w * y)
    b = w * y // gcd(h * x, w * y)
    print(((a * w) ** 2 + (b * h) ** 2) ** 0.5)
    print(a + b - 2)
    print('BT'[b % 2] + 'LR'[a % 2])
