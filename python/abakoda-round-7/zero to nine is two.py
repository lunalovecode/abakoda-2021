c = input().split("")
digit_len = int(c[0])
num_count = int(c[1])

num_list = []

for i in range(num_count):
    num_list = input()

segments = ["ABCDEF", "EF", "ACDFG", "ADEFG", "BEFG", "ABDEG", "ABCDEG", "AEF", "ABCDEFG", "ABDEFG"]

def flip_segment(src, target, flipped):
    letters = "ABCDEFG"
    for j in letters:
        if (j in patterns[src]) and (j in patterns[target]):
            continue
        
        if (not j in patterns[src]) and (not j in patterns[target]):
            continue
        
        flipped[j] = True
    }
}

mininum = ""
first = num_list[0]
for j in range(num_count):
    target = num_list[j]
    total_flipped = 0
    for k in range(digit_len):
        flipped_letters = {}
        flip_segment(int(first[k]), int(target[k]), flipped_letters)
        total_flipped += len(dict.keys(flipped_letters))
        
        if minimum == "":
            minimum = total_flipped
        
        if minimum >= total_flipped:
            minimum = total_flipped

print(minimum)