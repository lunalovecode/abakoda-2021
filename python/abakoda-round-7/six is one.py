b = input()
patterns = ["1111110", "0000110", "1011011", "1001111", "0100111", "1101101", "1111101", "1000110", "1111111", "1101111"]
if b in patterns:
    print(patterns.index(b))
else:
    print("!")