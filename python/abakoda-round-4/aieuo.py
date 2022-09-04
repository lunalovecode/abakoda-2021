def is_equivalent(a, b):
	if (a == b) or (a == "e" and b == "i") or (a == "i" and b == "e") or (a == "o" and b == "u") or (a == "u" and b == "o"):
		return True
	else:
		return False

r = input().split()
first_list = []
second_list = []

for i in range(len(r[0])):
	first_list[i] = list(r[0])[i]

for i in range(len(r[1])):
	second_list[i] = list(r[1])[i]

greater_list = first_list

if len(first_list) < len(second_list):
	greater_list = second_list

ans = []

for i in range(len(greater_list)):
	if is_equivalent(first_list[i], second_list[i]):
		ans.append(True)
	else:
		ans.append(False)

	if len(first_list) != len(second_list):
		ans.append(False)

all_true = all(ans)

if all_true:
	print("yis")
else:
	print("nuu")