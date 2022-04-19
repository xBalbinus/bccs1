#Dictionaries
#Key - value pairs
#Insert / remove key value pairs
#lookup, test does key exist

class Dict:
    def __init__(self, size=10):
        self.storage = [[] for _ in range(size)]
        self.size = size
        self.length = 0
        
    def __setitem__(self, key, value):
        storage_idx = hash(key) % self.size
        for ele in self.storage[storage_idx]:
            if key == ele[0]:
                ele[1] = value
                break
        else:
            self.storage[storage_idx].append([key, value])
            self.length += 1
            
    def __getitem__(self, key):
        storage_idx = hash(key) % self.size
        for ele in self.storage[storage_idx]:
            if ele[0] == key:
                return ele[1]
        raise KeyError("None".format(key))

    def __len__(self):
        return(self.length)

    def __contains__(self, key):
        storage_idx = hash(key) % self.size
        for item in self.storage[storage_idx]:
            if item[0] == key:
                return True
        return False
    
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        command = input()
        if command == "create":
            dict = Dict()
            continue
        if command.startswith("add") == True:
            keystore = command.split(" ")
            key = keystore[1]
            value = keystore[1]
            dict.__setitem__(key, value)
            continue
        if command.startswith("contains") == True:
            containsStore = command.split(" ")
            target = containsStore[1]
            dict.__contains__(target)
            continue