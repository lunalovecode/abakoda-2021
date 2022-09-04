a = [*input()]

def convert_to_int(n):
    return int(n)

row_1 = map(convert_to_int, input().split())
row_2 = map(convert_to_int, input().split())
row_1_points = sum(row_1)
row_2_points = sum(row_2)

if row_1_points > row_2_points:
    print(row_1_points)
else:
    print(row_2_points)