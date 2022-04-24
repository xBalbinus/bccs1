#https://leetcode.com/problems/length-of-last-word/submissions/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return (len(s[len(s)-1]))