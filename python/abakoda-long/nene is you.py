r,c = map(int,input().split())
arr_1 = [0] * 26
arr_2 = [0] * 26
moves = []
for _ in range(r):
  for i in input():
    arr_1[ord(i) - 65] = 1
    arr_2[ord(i) - 65] = 1
for _ in range(int(input())):
  x,__,y = map(str,input().split())
  if arr_2[ord(x)-65] == 1:
    arr_2[ord(x)-65] = 0
    arr_2[ord(y)-65] = 1
    moves.append([x, y])
if arr_1.count(1) != arr_2.count(1):
  print('NO')
else:
  print("YES")
  print(len(moves))
  for i in moves[::-1]:
    print(f'{i[1]} is {i[0]}')