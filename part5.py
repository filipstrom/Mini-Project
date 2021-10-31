import BstMap as bst
import os
import time


map = bst.BstMap()
#for n in lst:
 #   map.put(n, 2)


def read_words(path):
    with open(path, "r",  encoding="utf-8") as file:
        lst = file.read().split()
        newlst = []
        for e in lst:
            if len(e):
                newlst.append(e)
    return newlst


def count_words(lst, percent):
    map = bst.BstMap()
    i = 0
    for n in lst:
        i += 1
        v = map.get(n)
        value = 1 if v is None else (v + 1)
        map.put(n, value)
        if i > (len(lst)*percent):
            return map
        if i % (int(len(lst)*percent))/100 == 0:
            print(i/len(lst)*percent * 100, "%")
    return map


def time_to_get(bist):
    start = time.time()
    for i in range(1000000):
        bist.get("()?!¨'´")
        #if i % (1000000/10) == 0:
        #    print(i/1000000 * 100, "%")
    return((time.time() - start)/1000000)


path_holy = os.getcwd() + "\\test_holy.txt"
path_eng = os.getcwd() + "\\test_100K.txt"


lst_eng_words = read_words(path_eng)
s01_bst = count_words(lst_eng_words, 0.001)
s1_bst = count_words(lst_eng_words, 0.01)
s10_bst = count_words(lst_eng_words, 0.1)
s20_bst = count_words(lst_eng_words, 0.2)
s30_bst = count_words(lst_eng_words, 0.3)
s40_bst = count_words(lst_eng_words, 0.4)
#s50_bst = count_words(lst_eng_words, 0.5)
#s60_bst = count_words(lst_eng_words, 0.6)
#s70_bst = count_words(lst_eng_words, 0.7)
#s80_bst = count_words(lst_eng_words, 0.8)
#s90_bst = count_words(lst_eng_words, 0.9)
#s100_bst = count_words(lst_eng_words, 1)

print("Detta är s1", time_to_get(s01_bst), s01_bst.size())
print("Detta är s1", time_to_get(s1_bst), s1_bst.size())
print("Detta är s1", time_to_get(s10_bst), s10_bst.size())
print("Detta är s2", time_to_get(s20_bst), s20_bst.size())
print("Detta är s3", time_to_get(s30_bst), s30_bst.size())
print("Detta är s3", time_to_get(s40_bst), s40_bst.size())
#print("Detta är s3", time_to_get(s50_bst), s50_bst.size())
#print("Detta är s3", time_to_get(s60_bst), s60_bst.size())
#print("Detta är s3", time_to_get(s70_bst), s70_bst.size())
#print("Detta är s3", time_to_get(s80_bst), s80_bst.size())
#print("Detta är s3", time_to_get(s90_bst), s90_bst.size())
#print("Detta är s3", time_to_get(s100_bst), s100_bst.size())
quit()

start = time.time()
for i in range(small_test):
    smallbst.get("()?!¨'´")
    if i % (small_test/10) == 0:
        print(i/small_test * 100, "%")
print((time.time() - start)/small_test)

start = time.time()
for i in range(medium_test):
    mediumbst.get("()?!¨'´")
    if i % (medium_test/10) == 0:
        print(i/medium_test * 100, "%")
print((time.time() - start)/medium_test)
print(mediumbst.max_depth())

start = time.time()
for i in range(big_test):
    bigbst.get("()?!¨'´")
    if i % (big_test/10) == 0:
        print(i/big_test * 100, "%")
print((time.time() - start)/big_test)
print((bigbst.max_depth()))