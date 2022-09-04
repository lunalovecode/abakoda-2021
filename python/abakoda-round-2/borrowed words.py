c = list(input().lower())
letters = ["c", "f", "j", "q", "v", "x", "z"]

ans = "PINOY"
for i in c:
	if i in letters:
		ans = "FOREIGN"

print(ans)