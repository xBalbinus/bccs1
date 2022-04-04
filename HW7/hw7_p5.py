class Stack:
    def __init__(self, length):
        
        #initialize empty array with length elements
        self.items = [0] * length
        
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
        if self.front == len(self.items)-1:
            return
        # If not empty, remove front index from array
        if self.front != len(self.items)-1: 
        #Move back to position & print
            self.front += 1
            print(self.items[self.front])
        #Set back to 0
            self.items[self.front] = 0
            
    def duplicateRemover(self, s: str) -> str:
        d={}
        for i in range(len(s)):
            d[s[i]]=i
        stack=[]
        for i,j in enumerate (s):
            if j not in stack:
                while stack and stack[-1]>j and d[stack[-1]]>i:
                    stack.pop()


                stack.append(j)
        return "".join(stack)   
            
            


if __name__ == "__main__":
    word = input()
    stack = Stack(len(word))
    stack.duplicateRemover(word)

    

    
    
        