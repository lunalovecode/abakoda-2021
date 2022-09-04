# Add non-full lines in lines list
# If any lines are omitted, print additional output based on number of lines omitted
lines = []
for i in range(20):
    cur_line = input()
    if cur_line != "##########":
        lines.append(cur_line)

cleared_lines = 20 - len(lines)

print("\n".join(lines))

if cleared_lines == 1:
    print("SINGLE!")
elif cleared_lines == 2:
    print("DOUBLE!!")
elif cleared_lines == 3:
    print("TRIPLE!!!")
elif cleared_lines == 4:
    print("QUAD!!!!")
elif cleared_lines > 4:
    print("SUPER QUAD!!!1!")