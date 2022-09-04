def solve(word):
    ans = 1
    for letter in word:
        if letter == "e":
            ans *= 2
        elif letter == "i":
            ans *= 2
        elif letter == "o":
            ans *= 2
        elif letter == "u":
            ans *= 2
    return ans;

print(solve(input()))