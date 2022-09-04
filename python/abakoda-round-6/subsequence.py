c = input()

def subsequence(original, target):
	i = 0
	j = 0

	while i < len(target):
		if j == len(original):
			return False

		if target[i] == original[j]:
			i += 1

		j += 1

	return True

if subsequence(c, "...---..."):
	print("SOS")
else:
	print("Hay SOS!")