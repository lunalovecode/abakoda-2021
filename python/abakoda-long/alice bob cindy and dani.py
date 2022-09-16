cast = ["Alice", "Bob", "Cindy", "Dani"]
present_cast = input().split()
for i in cast:
	if i not in present_cast:
		print(i)
		break