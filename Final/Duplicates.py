#https://leetcode.com/problems/contains-duplicate/submissions/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #A set is a data type that does not contain duplicates.
        #Therefore, comparing the number of entries in a set to the number of entries
        #in a list will tell us if the list contains only unique numbers.
        return len(set(nums)) != len(nums)