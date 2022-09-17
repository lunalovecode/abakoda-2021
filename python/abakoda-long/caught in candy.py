import math
n, h, k = [int(x) for x in input().split()]
coords = [[0, 0] for i in range(n)]
def point_in_circle(point_coords, center_coords, radius):
    if math.dist(point_coords, center_coords) <= radius:
        return True
    else:
        return False

for i in range(n):
    x, y = [int(j) for j in input().split()]
    coords[i] = [x, y]

final_diameter = 0

def all_in_circle(coords_arr, radius):
    lst = [False for i in range(n)]
    for i in range(n):
        if point_in_circle(coords_arr[i], [h, k], radius):
            lst[i] = True
    return all(lst)

# increase final_diameter by 1 forever
# if one point is in the circle, add True to lst

while True:
    final_diameter += 1
    if all_in_circle(coords, final_diameter / 2):
        print(float(final_diameter))
        break