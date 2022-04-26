#https://leetcode.com/problems/next-greater-element-i/submissions/
#Monotonic stack / hashmap

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Create a dictionary of the next greatest number
        nextGreaterDict = {}
        #Create decreasing monotonic stack
        monoStack = []
        
        #pop from monoStack all the numbers x that are smaller than num and for each of those set nextGreaterDict[x] = num, then add num to the top of the stack
        for num in nums2:
            while monoStack and num > monoStack[-1]:
                nextGreaterDict[monoStack.pop()] = num
            monoStack.append(num)
                
        #Since we won't be using nums1 again, we can overwrite nums1[i] with its next greater element to save memory.
        #If there is an entry in the dictionary, slap on the value. Otherwise, get -1.
        for i, num in enumerate(nums1):
            nums1[i] = nextGreaterDict.get(num, -1)
            
        return nums1
    
#Driver code for python tutor    
#Solution.nextGreaterElement([4,1,2], [4,1,2], [1,3,4,2])