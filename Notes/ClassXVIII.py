#Implementing classes, intro to object oriented programming

class Stack:
    #This is the initialization. All others will be methods.
    def __init__(self):
        #To define the create function for a stack...
        self.__A = [0]
        self.__top = 0
        self.__size = 1
        #Adding __ to variables protects the data, 
        #which disables users from accessing the data in this class afterwards
    def push(self, v):
        if self.__top == self.__size:
            self.size *= 2
            tmp = [0] * self.__size
            for i in range(top):
                tmp[i] = self.__A[i]
            self.__A = tmp
        self.__A[self.__top] = v
        self.__top += 1
    def pop(self):
        self.__top -= 1
        return self.__A(self.__top)
    #In classes, you have some special functions such as __len__ that allow you to use special syntax.
    def __len__(self):
        return self.__top
    

def solution(s):
    N = len(s)
    #stack = create(N)
    stack = Stack()
    
    for i in range(N):
        c = s[i]
        
        if c == '(' or c =='{' or c =='[':
            stack.push(c)
        else:
            if len(stack) == 0:
                return False
            v_top = stack.pop()
            if not match(v_top,c):
                return False
            
    return len(stack) == 0
# return stack.__len__() == 0
        
        