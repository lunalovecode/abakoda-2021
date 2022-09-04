forbidden = input();
normal_forbidden = forbidden.split();
forbidden_lowercase = forbidden.toLowerCase().split();
sentence = input();
words = sentence.split(" ");
final_sentence = [];
def has_common_els(list_1, list_2):
    result = False
    for x in list_1:
        for y in list_2:
            if x == y:
                result = True
                return result
    return result



def censor(string):
    new_string = [];    
    for i in range(len(string)):
        new_string.append("*");
    
    return "".join(new_string);


for i in len(words):
    if has_common_els(words[i].split(), normal_forbidden) or has_common_els(words[i].split(), forbidden_lowercase):
        final_sentence.append(censor(words[i]));
     else:
        final_sentence.append(words[i]);
    

print(" ".join(final_sentence));