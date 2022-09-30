from collections import deque
 
m = int(input())
 
if m == 7:
    print('''24
AAAAAAAAAAAAAAAAAABBBBBB
AAAAAAAAAAAAAAAAAABBBBBB
AAAAAAAAAAAAAAAAAABBBBBB
AAAAAAAAAAAAAAAAAABBBBBB
AAAAAAAAAAAAAAAAAABBBBBB
AAAAAAAAAAAAAAAAAABBBBBB
AAAAAAAAAAAAAAAAAABBBBBB
AAAAAAAAAAAAAAAAAABBBBBB
AAAAAAAAAAAAAAAAAABBBBBB
AAAAAAAAAAAAAAAAAACCCCCC
AAAAAAAAAAAAAAAAAACCCCCC
AAAAAAAAAAAAAAAAAACCCCCC
DDDDDDDDDDDDDDDDDDCCCCCC
DDDDDDDDDDDDDDDDDDCCCCCC
DDDDDDDDDDDDDDDDDDCCCCCC
DDDDDDDDDDDDDDDDDDCCCCCC
DDDDDDDDDDDDDDDDDDCCCCCC
DDDDDDDDDDDDDDDDDDCCCCCC
DDDDDDDDDDDDDDDDDDEEEEFF
DDDDDDDDDDDDDDDDDDEEEEFF
DDDDDDDDDDDDDDDDDDEEEEFF
DDDDDDDDDDDDDDDDDDEEEEGG
DDDDDDDDDDDDDDDDDDEEEEGG
DDDDDDDDDDDDDDDDDDEEEEGG''')
    exit()


if m % 3 == 0:
    S = 512 * 3
    grid = deque([(0,0,256,'A'),(512,0,256,'B'),(1024,0,256,'C'),(0,256 * 3,256,'D'),(512,256 * 3,256,'E'),(1024,256 * 3,256,'F')])
    m -= 6
elif m % 3 == 1:
    S = 512 * 3
    grid = deque([(128 * 8,0,128 * 2,'I'),(128 * 8,128 * 6,128 * 2,'J'),(0,0,64 * 6,'A'),(0,64 * 18,64 * 2,'B'),(128 * 2,64 * 18,64 * 2,'C'),(128 * 4,64 * 18,64 * 2,'D'),(128 * 6,64 * 18,64 * 2,'E'),(128 * 6,64 * 12,64 * 2,'F'),(128 * 6,64 * 6,64 * 2,'G'),(128 * 6,0,64 * 2,'H')])
    m -= 10
elif m % 3 == 2:
    S = 128 * 18
    grid = deque([(0,0,128 * 4,'A'),(0,128 * 12,128 * 2,'B'),(128 * 4,128 * 12,128 * 2,'C'),(128 * 8,128 * 12,128 * 2,'D'),(128 * 8,128 * 6,128 * 2,'E'),(128 * 8,0,128 * 2,'F'),(128 * 12,0,128 * 3,'G'),(128 * 12,128 * 9,128 * 3,'H')])
    m -= 8
 
print(S)
 
for _ in range(m // 3):
    x,y,s,c = grid.popleft()
    if s % 2 == 1: exit()
    if c in 'STUV':
        grid.append((x,y,s // 2,'W'))
        grid.append((x+2 * s // 2,y,s // 2,'X'))
        grid.append((x,y+3 * s // 2,s // 2,'Y'))
        grid.append((x+2 * s // 2,y+3 * s // 2,s // 2,'Z'))
    elif c in 'OPQR':
        grid.append((x,y,s // 2,'S'))
        grid.append((x+2 * s // 2,y,s // 2,'T'))
        grid.append((x,y+3 * s // 2,s // 2,'U'))
        grid.append((x+2 * s // 2,y+3 * s // 2,s // 2,'V'))
    else:
        grid.append((x,y,s // 2,'O'))
        grid.append((x+2 * s // 2,y,s // 2,'P'))
        grid.append((x,y+3 * s // 2,s // 2,'Q'))
        grid.append((x+2 * s // 2,y+3 * s // 2,s // 2,'R'))
 
ans = [['.'] * (S) for _ in range(S)]
for x,y,s,c in grid:
    for x2 in range(x,x+2 * s):
        for y2 in range(y,y+3 * s):
            ans[x2][y2] = c
 
print('\n'.join(''.join(i) for i in ans))
 
 
 
def debug():
    from PIL import Image
    img = Image.new('RGB',(128 * 18,128 * 18))
    pix = img.load()
    for x in range(128 * 18):
        for y in range(128 * 18):
            pix[y,x] = ((ord(ans[x][y])-ord('S')) * 36,) * 3
    img.show()
