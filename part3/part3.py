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
    i = 0
    values = []
    keys = []
    for n in lst:
        i += 1
        if n in keys:
            values[keys.index(n)] += 1
        else:
            keys.append(n)
            values.append(1)
        #if i % 1000 == 0:
            #print(i, "nästan klar")
        
    for i in range(len(keys)):
        map.put(keys[i], values[i])
    return map

# Highest value in dictonary and print the key
def most_common(bist, n):
    word_tuples = bist.as_list()
    valueSorted = (sorted(word_tuples, key=lambda word: word[1]))[::-1]
    for k, v in valueSorted[:n]:
        print(k, "    \t", v)


# Getting the paths
path_holy = os.getcwd() + "\\part3\\holy_grail_words.txt"
path_eng = os.getcwd() + "\\part3\\eng_news_words.txt"


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
