n = int(input())
words = [input() for i in range(n)]
pattern = input()

def match(word, patt):
    ans_arr = [False for i in range(len(patt))]
    # check if the non-underscore letters match are in the same position
    for i in range(len(patt)):
        if word[i] == patt[i] or patt[i] == "_":
            ans_arr[i] = True
    
    if all(ans_arr):
        return True
    else:
        return False

ans = "!"

for i in words:
    if match(i, pattern):
        ans = i
        break

print(ans)