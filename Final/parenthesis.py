#we did this in class too, https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        #Create a mapping D between the opening and closing brackets
        d = {'(':')', '{':'}','[':']'}
        #Initialize a stack
        stack = []
        #For each entry in the stack
        for i in s:
            #If the entry is in d, append to stack
            if i in d:  
                stack.append(i)
            #else, if the length of the stack is zero, or the entry previous is not the corresponding closing bracket (e.g. {)), return False
            elif len(stack) == 0 or d[stack.pop()] != i:  
                return False
        #Check if the final length of the stack is 0
        return len(stack) == 0 