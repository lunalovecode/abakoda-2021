d = int(input())
people = []
for i in range(d):
    enter, exit = [int(x) for x in input().split()]
    people.append([enter, exit, i + 1])

def borrow_time(person):
    enter, exit, index = person
    return exit - enter

def compatible(p1_enter, p1_exit, p2_enter, p2_exit):
    if (p1_exit <= p2_enter) or (p2_exit <= p1_enter):
        return False
    else:
        return True

people.sort(key=borrow_time)

people_chosen = []
for enter, exit, index in people:
    able = True
    for other_enter, other_exit, other_index in people_chosen:
        if not compatible(enter, exit, other_enter, other_exit):
            able = False
    if able:
        people_chosen.append([enter, exit, index])

ans = []
for j in range(len(people_chosen)):
    ans.append(str(people_chosen[j][2]))
print(" ".join(ans))