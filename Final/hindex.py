#https://leetcode.com/problems/h-index/submissions/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #h index
        n = len(citations) + 1
        arr = [0] * n
        #Initialized array with 0 entries, length of the citations list + 1
        #Iterating through the citations list to +1 to the new array's entry if C is greater than n
        for c in citations:
            if c >= n:
                arr[n-1] += 1
            else:
                arr[c] += 1
        
        total = 0
        #Iterating backward thru the list
        #Count the index - when the index is greater than the number of total citations that's when we know that the index number is the h-index
        #Example: In an array of (0, 1, 2, 3, 4, 5) for the different numbers of citations the author can get
        #Let's say if there are (0, 1, 1, 1, 1, 2) works of that amount cited
        # 3 would be the h-index here because 1+2 >= 3
        for i in range(n-1, -1, -1):
            total +=  arr[i]
            if total >= i:
                return i
        
        return 0        