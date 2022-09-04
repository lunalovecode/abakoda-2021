b = input().split()
n = int(b[0])
def convert_to_int(n):
    return int(n)

row_1 = [int(x) for x in input().split()]
row_2 = [int(x) for x in input().split()]

for i in range(len(row_1)):
    row_1[i] = int(row_1[i])

ans = 0

for j in range(n):
    ans += max(row_1[j], row_2[j])

print(ans)