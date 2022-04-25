#https://leetcode.com/problems/maximum-product-subarray/submissions/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Similar to the maximum sum subarray
        #Divide / conquer approach
        m=-inf
        po=-inf 
		#     po here is maximum product so far
        ne=inf
		#     ne here is minimum product so far
        for e in nums:
            if e<0:
                po,ne=max(ne*e,e),min(po*e,e)
            else:
                po,ne=max(e,po*e),min(e,ne*e)
            m=max(m,po)    
        return m