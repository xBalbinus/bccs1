#All variables, when assigned to numbers (which are all objects in python)
#Are considered as REFERENCES to the object.

#Nodes! Essentially just data pointers. A data type that contains data points to another node (or more).

class Node:
    def __init__(self, v, tl):
        self.value = v
        self.tl = tl
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, v):
        new_node = Node(v, self.head)
        self.head = new_node
        self.size += 1
    
    def pop(self):
        v = self.head.value
        self.head = self.head.tail
        self.size -= 1
        return v
    
    def __len__(self):
        return self.size
    
#Queue - insert a bunch of values, fetches the OLDEST value entered (emqueue, dequeue)

#List - Everyone has an index, index starts at 0, initialize via. [];
# .append for adding values to the end of a list. O(1)
# insert for insertion values O(n)
# python docs has documentation on amortized worst case operation time.

#Set - Add, remove, is x in set or not (similar to sets in math). 
#Operations such as Union / Intersection are also available. Set elements are not ordered

#Dictionary - key value pairs (e.g. keys are words, values are definitions in a traditional dictionary)
#Operations: insert, look up
#e.g. d['joe'] = b, calling d['joe'] would return b
#e.g. 'joe' in d would return True