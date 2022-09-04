n = int(input())
nums = {"a": 0, "b": 0, "k": 0, "d":0}

def get_count(lst, value):
	count = 0
	if value in lst:
		count = count + 1
	return count

for i in range(n):
	lines = [*input()]
	nums["a"] = nums["a"] + get_count(lines, "A")
	nums["b"] = nums["b"] + get_count(lines, "B")
	nums["k"] = nums["k"] + get_count(lines, "K")
	nums["d"] = nums["d"] + get_count(lines, "D")

print(str(nums["a"]) + " " + str(nums["b"]) + " " + str(nums["k"]) + " " + str(nums["d"]))