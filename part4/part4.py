import matplotlib.pyplot as plt
import HashSet as hs
import BstMap as bst
import os


def read_words(path):
    with open(path, "r",  encoding="utf-8") as file:
        lst = file.read().split()
        newlst = []
        for e in lst:
            if len(e):
                newlst.append(e)
    return newlst


def words_length_count(lst):
    map = bst.BstMap()
    for n in lst:
        v = map.get(len(n))
        value = 1 if v is None else (v + 1)
        map.put(len(n), value)
    return map


def plot_word_length(bst, string):
    lst = bst.as_list()
    lstx = []
    lsty = []
    for i in lst:
        lstx.append(i[0])
        lsty.append(i[1])
    plt.bar(lstx, lsty)
    plt.xticks(lstx, lstx) # Give each position a label
    plt.title('words per wordlength for ' + string)
    plt.xlabel("word length")
    plt.ylabel("word count")
    plt.show()

def unique_words(lst, title):
    words = hs.HashSet()   # Create new empty HashSet
    words.init()
    lsty = []
    i = 0
    size = 0
    for w in lst:
        i += 1
        if not words.contains(w):
            words.add(w)
            size += 1
        lsty.append(size)
    plt.plot([n for n in range(len(lsty))], lsty)
    plt.title('"added words" vs "unique words" in ' + title)
    plt.xlabel("added words")
    plt.ylabel("unique words")
    plt.show()

path_holy = os.getcwd() + "\\part1\\test_holy.txt"
path_eng = os.getcwd() + "\\part1\\test_100K.txt"

holy_words = read_words(path_holy)
eng_words = read_words(path_eng)
holy_bst = words_length_count(holy_words)
eng_bst = words_length_count(eng_words)

plot_word_length(holy_bst, "monty python")
plot_word_length(eng_bst, "English 100K")


unique_words(holy_words, "monty python")
unique_words(eng_words, "English 100K")
