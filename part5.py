import BstMap as bst
import os
import time
import matplotlib.pyplot as plt
import HashSet as hs
input()


def read_words(path):
    with open(path, "r",  encoding="utf-8") as file:
        lst = file.read().split()
        newlst = []
        for e in lst:
            if len(e):
                newlst.append(e)
    return newlst


def menu():
    choices = ["plot: look-up time vs tree size and max depth vs tree size",
               "plot: how the max bucket size changes with the set sizes"]
    for i in range(len(choices)):
        print(str(i+1) + ": " + choices[i])
    choice = input()
    if choice == "1":
        part1()
    if choice == "2":
        part2()
    if choice != "stop":
        print("Choose one of the options")
        menu()


def part2():
    print("Part 2")
    time_lst = []
    maxbucket_lst = []
    set_size_lst = []
    hash_set = hs.HashSet()
    hash_set.init()
    for e in range(len(lst_eng_words)):
        if e % 1000 == 0:
            set_size_lst.append(e)
            for i in range(1000):
                start_time = time.time()
                hash_sett_copy = hash_set
                hash_sett_copy.add(lst_eng_words[e-1000])
                sum_time = time.time() - start_time
            time_lst.append(sum_time/1000)
        hash_set.add(lst_eng_words[e])

        if e % 1000 == 0:
            print(e / len(lst_eng_words) * 100)
            maxbucket_lst.append(hash_set.max_bucket_size())
    plt.subplot(1, 2, 1)
    plt.plot(set_size_lst, time_lst)
    plt.title('"time to add element" vs "hashset size"')
    plt.xlabel("hashset size")
    plt.ylabel("time")

    plt.subplot(1, 2, 2)
    plt.plot(set_size_lst, maxbucket_lst)
    plt.title('"maxbucket size" vs "hashset size" in ' + "eng=")
    plt.xlabel("hashset size")
    plt.ylabel("maxbucket size")
    plt.show()


def part1():
    print("Part 1")
    lst = []
    for i in range(0, 20, 1):
        print(i/100)
        lst.append(count_words(lst_eng_words, i/100))

    timetoget_lst = []
    max_tree_depth = []
    tree_size = []
    for e in lst:
        timetoget_lst.append(time_to_get(e))
        max_tree_depth.append(e.max_depth())
        tree_size.append(e.size())

    # plot time to get:
    plt.subplot(1, 2, 1)
    plt.plot(tree_size, timetoget_lst)
    plt.title('"time to get" vs "tree size" in ')
    plt.xlabel("tree size")
    plt.ylabel("time")
    plt.subplot(1, 2, 2)
    plt.plot(tree_size,  max_tree_depth)
    plt.title('"max tree depth" vs "tree size"')
    plt.xlabel("tree size")
    plt.ylabel("max tree depth")
    plt.show()


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
        if i % (len(lst)/100) == 0:
            print(i/len(lst) * 100, "%")
    return map


def time_to_get(bist):
    start = time.time()
    for i in range(int(1000000)):
        bist.get("()?!¨'´")
    return((time.time() - start)/1000000)


path_eng = os.getcwd() + "\\test_100K.txt"
input("fds")
lst_eng_words = read_words(path_eng)
input("nu är det kört")
menu()
