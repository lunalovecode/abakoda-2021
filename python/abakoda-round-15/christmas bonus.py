friends = int(input())
pieces = int(input())
x = int(input())
y = int(input())

if friends == 1:
    print("IMPOSSIBLE")
else:
    print(y % friends)