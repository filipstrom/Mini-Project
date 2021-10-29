import sys
import HashSet as hs
import BstMap as bst
import os


# Reads all the words and returns a list
def read_words(path):
    with open(path, "r",  encoding="utf-8") as file:
        lst = file.read().split()
        newlst = []
        for e in lst:
            if len(e) > 4:
                newlst.append(e)
    return newlst


# Counts the amount of accourenses for all the words
def count_words(lst):
    map = bst.BstMap()
    for n in lst:
        v = map.get(n)
        value = 1 if v is None else (v + 1)
        map.put(n, value)
    return map


# Highest value in dictonary and print the key
def most_common(bist, n):
    word_tuples = bist.as_list()
    valueSorted = (sorted(word_tuples, key=lambda word: word[1]))[::-1]
    for k, v in valueSorted[:n]:
        print(k, "    \t", v)


def make_HashSet(lst):
    hash_set = hs.HashSet()
    hash_set.init()
    for e in lst:
        hash_set.add(e)
    return hash_set


def info_print(path, title):
    # Unique words and 10 most used words in Holy grail
    print("_________________________")
    print("     " + title)
    words_lst = read_words(path)
    hash_set = make_HashSet(words_lst)
    print("Hash set size:", hash_set.get_size())
    print("Max bucket size:", hash_set.max_bucket_size())

    # Getting the most common
    bst = count_words(words_lst)
    print("Max depth in bst:", bst.max_depth())
    most_common(bst, 10)


# Getting the paths
path_holy = os.getcwd() + "\\test_holy.txt"
path_eng = os.getcwd() + "\\test_100K.txt"
info_print(path_holy, "holy_grail_words.txt")
info_print(path_eng, "Eng_news_words.txt")