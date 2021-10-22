
# Open the file and
def read_rows(file_path):
    file = open(file_path, encoding='utf-8')
    lines = file.readlines()
    file.close()
    return lines
# Find every word in a row


def get_words(rows, lenght):
    words = []
    for row in rows:
        for word in row.lower().split():
            newword = ""
            for c in word:
                newword += c.strip("1234567890!?#&.,_|\n:;()%¤$—–-•’”“")
            if newword != "":
                if len(newword) > lenght:
                    words.append(newword)
    return words


# GetValue?
def get_value(tpl):
    return tpl[1]


# Higest value in dictonary and print the key
def most_common(dct, n):
    items = list(dct.items())
    valueSorted = (sorted(items, key=get_value))[::-1]
    for k, v in valueSorted[:n]:
        print(k, "\t", v)


# Count occurenses in list
def count_occurrences(lst):

    dct = {}
    for item in lst:
        if item in dct:
            dct[item] += 1
        else:
            dct[item] = 1
    return dct


# Count different
def count_different(lst):
    return len(set(lst))
