r, c = [int(i) for i in input().split()]
grid = []
for i in range(r):
    grid.append(input())

for j in range(int(input())):
    key = input()
    print("---")
    not_word = ["*" * c for i in range(r)]
    ln = len(key)
    for k in range(c):
        for l in range(r):
            if grid[l][k] == key[0]:
                e = k > ln - 2
                f = l > ln - 2
                g = k + ln <= c
                h = l + ln <= r
                if e:
                    for i in range(1, ln):
                        if a[l][k - i] != key[i]:
                            break
                        else:
                            for i in range(ln):
                                not_word[l][k - i] = key[i]
                if f:
                    for i in range(1, ln):
                        if a[l - i][k] != key[i]:
                            break
                        else:
                            for i in range(ln):
                                not_word[l - i][k] = key[i]
                if g:
                    for i in range(1, ln):
                        if grid[l][k + i] != key[i]:
                            break
                        else:
                            for i in range(ln):
                                not_word[l][k + i] = key[i]
                if h:
                    for i in range(1, ln):
                        if grid[l + i][k] != key[i]:
                            break
                        else:
                            for i in range(ln):
                                not_word[l + i][k] = key[i]
                
                if e and f:
                    for i in range(1, ln):
                        if grid[l - i][k - i] != key[i]:
                            break
                        else:
                            for i in range(ln):
                                not_word[l - i][k - i] = key[i]
                if e and h:
                    for i in range(1, ln):
                        if grid[l + i][k - i] != key[i]:
                            break
                        else:
                            for i in range(ln):
                                not_word[l + i][k - i] = key[i]
                if g and f:
                    for i in range(1, ln):
                        if grid[l - i][k + i] != key[i]:
                            break
                        else:
                            for i in range(ln):
                                not_word[l - i][k + i] = key[i]
                if g and h:
                    for i in range(1, ln):
                        if grid[l + i][k + i] != key[i]:
                            break
                        else:
                            for i in range(ln):
                                not_word[l + i][k + i] = key[i]
    for i in range(r):
        print("".join(not_word(i)))