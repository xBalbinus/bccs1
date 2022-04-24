#https://leetcode.com/problems/plus-one/submissions/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #convert numbers to string then join
        newnumber = int("".join(map(str, digits)))
        #next, add 1
        plusoneint = newnumber + 1
        #split back
        newdigits = [int(i) for i in str(plusoneint)]
        return (newdigits)