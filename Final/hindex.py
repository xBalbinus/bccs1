#https://leetcode.com/problems/h-index/submissions/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #h index
        n = len(citations) + 1
        arr = [0] * n
        for c in citations:
            if c >= n:
                arr[n-1] += 1
            else:
                arr[c] += 1
        
        total = 0
        for i in range(n-1, -1, -1):
            total +=  arr[i]
            if total >= i:
                return i
        
        return 0