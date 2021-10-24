import os


# GetValue?
def get_value(tpl):
    return tpl[1]


# Highest value in dictonary and print the key
def most_common(dct, n):
    items = list(dct.items())
    valueSorted = (sorted(items, key=get_value))[::-1]
    for k, v in valueSorted[:n]:
        print(k, "    \t", v)


# Reads all the words and returns a list
def read_words(path):
    with open(path, "r", encoding="utf-8") as file:
        lst = file.read().split()
        newlst = []
        for e in lst:
            if len(e) > 4:
                newlst.append(e)
        print("Unique words: ", len(set(lst)))
    return newlst


# Counts the word usage in lst with a dictonary
def count_words(lst):
    dct = {}
    for n in lst:
        if n in dct:
            dct[n] += 1
        else:
            dct[n] = 1
    return dct


path_holy = os.getcwd() + "\\part1\\test_holy.txt"
path_eng = os.getcwd() + "\\part1\\test_100K.txt"
# Unique words and 10 most used words in Holy grail
lst = read_words(path_holy)
dct = count_words(lst)
most_common(dct, 10)
print()

# Unique words and 10 most used words in Eng News
lst = read_words(path_eng)
dct = count_words(lst)
most_common(dct, 10)
