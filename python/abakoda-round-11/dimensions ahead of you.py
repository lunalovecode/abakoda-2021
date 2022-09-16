a, b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

freq = {}
for v in c:
    if v not in freq:
        freq[v] = 0
    freq[v] += 1

total = 0
for i in range(a):
    for j in range(a):
        if i != j:
            total += freq[b - c[i] * c[j]]
    
    if b - c[i] * c[j] == c[i]:
        total -= 1
    
    if b - c[i] * c[j] == c[j]:
        total -= 1
print(total)