from collections import deque
from sys import stdin, stdout
input = stdin.readline
print = stdout.write
 
n, m = (int(i) for i in input().split())
names = {i:-1 for i in input().split()}
visit = {i:False for i in names}
links = {i:[] for i in names}
group = []
 
for i in range(m):
    input()
    org = input().split()
    for member in org: links[member].append(i)
    group.append(org)
 
alice = "Alice"
names[alice] = 0
visit[alice] = True
 
queue = deque()
queue.append(alice)
 
while queue:
    source = queue.popleft()
    depth = names[source] + 1
    for idx in links[source]:
        for member in group[idx]:
            if not visit[member]:
                queue.append(member)
                visit[member] = True
                names[member] = depth
        group[idx].clear()
 
print(" ".join((str(i) for i in names.values())))