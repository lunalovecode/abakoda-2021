a = int(input())

def create_combo(n, t):
    return [n, (t - n)]

def count_combos(n):
    combinations = []
    for i in range(1, n):
        combinations.append(create_combo(i, n))
    
    for j in combinations:
        if combinations[0] == combinations[1]:
            combinations.remove(combinations[j])
    
    return len(combinations)

print(count_combos(a))