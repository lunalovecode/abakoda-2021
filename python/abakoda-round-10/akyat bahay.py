def consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst) + 1))

def convert(lst):
    return int(n)

a = input().split()
b = map(convert, a)
if (consecutive(a)):
    print("Yes")
else:
    print("No")