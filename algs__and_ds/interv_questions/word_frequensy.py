import re

string = "So feel been kept be at gate. Be september it extensive oh concluded of certainty. In read most gate at body held it ever no. Talking justice welcome message inquiry in started of am me. Led own hearted highest visited lasting sir through compass his. Guest tiled he quick by so these trees am. It announcing alteration alteration at surrounded comparison."

def word_freq(string):
    list_of_words = [word.lower() for word in re.sub('[^ a-zA-Z]+', '', string).split()]

    temp = set()
    repeated_words = []

    for word in list_of_words:
        if word in temp:
            repeated_words.append(word)
        else:
            temp.add(word)

    return repeated_words

# alter

# for word in list_of_words:
#     temp[word] = 0
# for word in list_of_words:
#     temp[word] = temp[word]+1

print(word_freq(string))