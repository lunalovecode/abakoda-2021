n = int(input())
a_0 = []
a_100 = []
a_200 = []
a_300 = []
a_400 = []
contestants = []

for i in range(n):
	r = input().split()
	if r[1] == "0":
		a_0.append(r[0])

	if r[1] == "100":
		a_100.append(r[0])

	if r[1] == "200":
		a_200.append(r[0])

	if r[1] == "300":
		a_300.append(r[0])

	if r[1] == "400":
		a_400.append(r[0])

if a_400:
	a_400.sort()
	for i in range(len(a_400)):
		print(a_400[i] + " 400")

if a_300:
	a_300.sort()
	for i in range(len(a_300)):
		print(a_300[i] + " 300")

if a_200:
	a_200.sort()
	for i in range(len(a_200)):
		print(a_200[i] + " 200")

if a_100:
	a_100.sort()
	for i in range(len(a_100)):
		print(a_100[i] + " 100")

if a_0:
	a_0.sort()
	for i in range(len(a_0)):
		print(a_0[i] + " 0")