from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hash_value = 0
        for c in word:
            hash_value += ord(c)
        return hash_value

    # Doubles size of bucket list
    def rehash(self):
        length = len(self.buckets)
        self.buckets.extend([[] for i in range(length)])
        lst = []
        for e in self.buckets:
            for o in e:
                lst.append(o)
        self.buckets = [[] for i in range(self.size*2)]
        self.size = 0

        for e in lst:
            self.add(e)

    # Adds a word to set if not already added

    def add(self, word):
        length = len(self.buckets)
        if self.size == length:
            self.rehash()
        position = self.get_hash(word) % length
        if word not in self.buckets[position]:
            self.buckets[position].append(word)
            self.size += 1

    # Returns a string representation of the set content

    def to_string(self):
        stri = "{ "
        for e in self.buckets:
            for s in e:
                stri += s + " "
            # stri += str(e) + " "
        stri += "}"
        return stri

    # Returns current number of elements in set

    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        for e in self.buckets:
            for s in e:
                if s == word:
                    return True
        return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):

        length = len(self.buckets)
        position = self.get_hash(word) % length
        if word in self.buckets[position]:
            self.buckets[position].remove(word)
            self.size -= 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        size = 0
        for element in self.buckets:
            if len(element) > size:
                size = len(element)
        return size
