t = int(input())
for i in range(t):
    f, s = [int(x) for x in input().split()]
    
    lst = []
    for j in range(4201):
        lst.append(False)
    
    k = 4200 - f
    c = 0
    
    while True:
        k -= s
        while k < 0:
            k += 4201
            
            if k == 4200:
                print(c)
                break
            elif lst[k]:
                print("NO HUGS")
            else:
                c += 1
                lst[k] = True
