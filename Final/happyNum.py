#https://leetcode.com/problems/happy-number/submissions/

class Solution:
    def isHappy(self, n: int) -> bool:
        #We can use a set here
        #The point of using a set is to detect when we've looped back to a  previously
        #seen number in the process of getting happy numbers
        falsifier = set()
        
        while n != 1:
            if n in falsifier:
                return False
            #add n to the list of numbers we've seen before
            falsifier.add(n)
            #sum of each digit in n squared.
            n = sum([int(i)**2 for i in str(n)])
       
        return True
        