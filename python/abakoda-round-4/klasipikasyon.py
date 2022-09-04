n = int(input())
words = set()
for i in range(n):
    word = input()
    word = word.replace("e", "i")
    word = word.replace("o", "u")
    words.add(word)
print(len(words))