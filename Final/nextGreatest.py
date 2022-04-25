#https://leetcode.com/problems/next-greater-element-i/submissions/
#Monotonic stack / hashmap

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreaterDict = {}
        monoStack = []
        
        for num in nums2:
            while monoStack and num > monoStack[-1]:
                nextGreaterDict[monoStack.pop()] = num
            monoStack.append(num)
                
        for i, num in enumerate(nums1):
            nums1[i] = nextGreaterDict.get(num, -1)
            
        return nums1