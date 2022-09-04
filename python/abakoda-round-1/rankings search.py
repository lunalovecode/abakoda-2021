n = int(input())
contestants = {}

for i in range(n):
	r = input().split()
	contestants[r[0]] = i

s = int(input())

for i in range(s):
	name = input()
	print(contestants[name] + 1)