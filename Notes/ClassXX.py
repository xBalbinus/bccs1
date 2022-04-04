#Dictionaries
#Key - value pairs
#Insert / remove key value pairs
#lookup, test does key exist

class KVP:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return str(self.key) + ' : ' + str(self.value)

#kv = KVP('Joe', 43), calling kv returns the place in memory
    
        

class LDict:
    def __init__(self):
        self.repr = []
    #Define this to gain access to the 'in' keyword
    #O(n)
    #O(log(N)) in balanced trees
    #By average case analysis, O(1)
    def __contains__(self, key):
        for kv in self.repr:
            if kv.key == key:
                return True
        return False
    #O(1)
    #Sorted list - O(n)
    #O(log(N)) - balanced trees
    def __setitem__(self, key, value):
        kv = KVP(key, value)
        self.repr.append(kv)
    #O(n)
    def __str__(self):
        s = ''
        for kv in self.repr:
            s += str(kv) + ' , '
        return s[:-2]
    #O(n)
    #O(log(N)) in ordered list
    #Balance trees - O(log(N))
    def __getitem__(self, key):
        for kv in self.repr:
            if kv.key == key:
                return kv.value

#Hash table - data structure for a dictionary.
#Hash function
# hash('Joe') returns an integer
# hash('Marie') returns a slightly different integer.
# You can then store this space of keys into an array.l
# To avoid 2 identical entries, you would do "chaining".
# Instead of storing values / key values directly into the array, every cell contains a list
# When you insert the key value pair, you would stick it into a list. you owuld then query the list in the individual cell.

    
        

        
        