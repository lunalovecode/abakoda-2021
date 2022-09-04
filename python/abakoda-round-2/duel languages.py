n = int(input())
def is_forbidden(c, forbidden):
    f = forbidden.split()
    for i in range(len(f)):
        if f[i] in c.upper():
            return True
        
    
    
    return False

 
def has_forbidden(s, forbidden):
    for c in s:
        if (is_forbidden(c, forbidden)):
            return True
        
    
    return False

 
abakoda_only = 0
hiram_only = 0
both = 0
 
for in range(n):
    r = input()
    hasAbakoda = has_forbidden(r, "ABKD")
    hasHiram = has_forbidden(r, "CFJQVXZ")
    
    if (hasAbakoda && hasHiram):
        both += 1
     else if (hasAbakoda):
        abakoda_only += 1
     else if (hasHiram):
        hiram_only += 1
    

 
ans = 0
ans += abakoda_only * hiram_only * both
ans += abakoda_only * both * (both - 1)
ans += both * hiram_only * (both - 1)
ans += both * (both - 1) * (both - 2)
 
print(ans)