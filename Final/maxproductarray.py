#https://leetcode.com/problems/maximum-product-subarray/submissions/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #We can do a sweep through the numbers of the array
        #Take into account the possibility of negative or 0 entries
        #We take into account the current #, product of the last and current
        #As well as the minimum so far and current (to counteract negatives)
        m = -inf
        po = -inf 
		#     po here is maximum product so far
        ne = inf
		#     ne here is minimum product so far
        for e in nums:
            if e < 0:
                po,ne=max(ne*e,e),min(po*e,e)
                print(po, ne)
            else:
                po,ne=max(e,po*e),min(e,ne*e)
                print(po, ne)
            m=max(m,po)    
            print(m)
        return m