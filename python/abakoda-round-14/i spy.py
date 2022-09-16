key = input()
guesses = [input() for i in range(4)]
print("W" if key in guesses else "L")