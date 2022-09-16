def func(arg1, arg2, f):
    return sum(f**k for k in range(arg1, arg2 + 1)) # I did this on purpose >:)

def solve(arg1, arg2, n):
    if arg2 == 1:
        return n
    
    est = int(n**(1 / arg2))
    for i in range(-10, 10 + 1):
        guess = est + i
        if guess >= 1 and func(arg1, arg2, guess):
            return guess

n = int(input())

for i in range(n):
    cur_case = [int(x) for x in input().split()]
    print(solve(cur_case[0], cur_case[1], cur_case[2]))