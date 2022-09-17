import itertools
n = int(input())
baskets = [int(x) for x in input().split()]
skill_levels = [int(x) for x in input().split()]
basket_arrangements = list(itertools.permutations(baskets))
skill_arrangements = list(itertools.permutations(skill_levels))
count = 0
def match(basket, skill):
    lst = []
    for i in range(len(basket)):
        if basket[i] <= skill_levels[i]:
            lst.append(True)
        else:
            lst.append(False)
    return all(lst)

for i in range(len(basket_arrangements)):
    if match(basket_arrangements[i], skill_arrangements[i]):
        count += 1

print(count)