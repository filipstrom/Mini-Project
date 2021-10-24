import sys
sys.path.insert(1, 'c:\\Users\\filip\\Programering\\python_courses\\1DV501\\mini-project\\part2')
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


# Getting the paths
path_holy = os.getcwd() + "\\part1\\test_holy.txt"
path_eng = os.getcwd() + "\\part1\\test_100K.txt"


# Unique words and 10 most used words in Holy grail
print("_________________________")
print("     holy_grail_words.txt")
lst_holy_words = read_words(path_holy)
holy_hash_set = hs.HashSet()
holy_hash_set.init()
for e in lst_holy_words:
    holy_hash_set.add(e)
print("Hash set size:", holy_hash_set.get_size())
print("Max bucket size:", holy_hash_set.max_bucket_size())

# Getting the most common
holy_bst = count_words(lst_holy_words)
print("Max depth in bts:", holy_bst.max_depth())
most_common(holy_bst, 10)




print("_________________________")
print("     Eng_news_words.txt")
lst_eng_words = read_words(path_eng)
eng_hash_set = hs.HashSet()
eng_hash_set.init()
for e in lst_eng_words:
    eng_hash_set.add(e)
print("Hash set size:", eng_hash_set.get_size())
print("Max bucket size:", eng_hash_set.max_bucket_size())

# Getting the most common
eng_bst = count_words(lst_eng_words)
print("Max depth in bts:", eng_bst.max_depth())
most_common(eng_bst, 10)
