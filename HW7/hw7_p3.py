class Stack:
    def __init__(self, length):
        
        #initialize empty array with length elements
        self.items = [None] * length
        
        #set front index pointer
        self.front = length - 1
        self.length = length
        
    def push(self, value):
        # Check queue is full or not
        if self.front == self.length:
            return
            
        # if not full
        else:
            self.items[self.front] = value
            # increment rear
            self.front -= 1
    
    def test_empty(self):
        for i in range(self.length):
            if self.items[i] != 0:
                print("False")
                break
            if i == self.length-1 and self.items[i] == 0:
                print("True")
            if self.items[i] == 0:
                continue
            
    # Function to delete an element from the front of the queue
    def pop(self):
        # Check if list, ie., items array is empty
        if self.front == len(self.items):
            return
        # If not empty, check if current entry is less than the previous entry, otherwise skip.
        for i in range (len(self.items)-2):
        #Move back to position & print if greater.
            if self.items[i+1] > self.items[i] and self.items[i] != 0:
                print(self.items[i])
                #Set back to 0
                self.items[i] = 0
                return
                
            
        
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        command = input()
        if command == "create":
            stack = Stack(100)
            continue
        if command == "test_empty":
            stack.test_empty()
            continue
        if command == "pop":
            stack.pop()
            continue
        else:
            stack.push(int(command))
            continue