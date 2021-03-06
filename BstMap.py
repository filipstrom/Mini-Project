from dataclasses import dataclass
from typing import Any, SupportsIndex

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key, value):
        if self.key == key:
            self.value = value
        if self.key < key:
            if self.right is None:
                self.right = Node(key, value, None, None)
            else:
                self.right.put(key, value)
        if self.key > key:
            if self.left is None:
                self.left = Node(key, value, None, None)
            else:
                self.left.put(key, value)
        

               # Placeholder code ==> to be replaced

    def to_string(self):
        string = ""
        if self.left is not None:
            string += self.left.to_string()
        string += f"({self.key},{self.value}) "
        if self.right is not None:
            string += self.right.to_string()
        string += ""

        return string
        # Placeholder code to avoid crash in demo program. To be replaced

    def count(self):
        size = 0
        if self.left is not None:
            size += self.left.count()
        size += 1
        if self.right is not None:
            size += self.right.count()
        return size


    def get(self, key):
        value = None
        if self.key == key:
            return self.value
        elif self.left is not None and self.key > key:
            value = self.left.get(key)
        elif self.right is not None and self.key < key:
            value = self.right.get(key)
        return value


    def max_depth(self):
        depth_left = 0
        depth_right = 0
        if self.left is not None:
            depth_left += self.left.max_depth()
        if self.right is not None:
            depth_right += self.right.max_depth()
        
        if depth_left > depth_right:
            return depth_left + 1
        else:
            return depth_right + 1
        pass     # Placeholder code ==> to be replaced

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        if self.left is not None:
            lst = self.left.as_list(lst)
        lst.append((self.key, self.value))
        if self.right is not None:
            lst = self.right.as_list(lst)
        return lst

        return [None]    # Placeholder code to avoid crash in demo program. To be replaced


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
