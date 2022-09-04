n = int(input())
def equivalent(word):
    return word.replace("e", "i").replace("u", "o")

word_list = set()

for i in range(n):
    word = input().lower()
    if str(equivalent(word)) in word_list:
        word_list.discard(equivalent(word))
    else:
        word_list.add(str(equivalent(word)))
        
print(len(word_list), sep='\n')

for j in word_list:
    print (''.join(j))