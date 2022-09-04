maybe_sos = []

def recurse(a, b, lst):
    if a == b:
        maybe_sos.append("".join(lst))
        return
    
    lst[a] = 0
    recurse(a + 1, b, lst)
    
    lst[a] = 5
    recurse(a + 1, b, lst)

c = 15
recurse(0, c, [None for i in range(c)])

counter = 0
a, b = map(int, input().split())
for i in maybe_sos:
    if a <= int(i) <= b and "505" in i:
        counter += 1
print(counter)