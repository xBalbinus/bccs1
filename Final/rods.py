#https://leetcode.com/problems/rings-and-rods/submissions/

class Solution:
    def countPoints(self, rings: str) -> int:
          #Pretty sure we did this one in class.
        #Use a dictionary here.
        rod = {}
        #Set up rods as keys
        for i in range(1, len(rings), 2):
            rod[rings[i]] = []
        #Create list of ring colors
        ringCounter = 0
        for i in range(1, len(rings), 2):
            rod[rings[i]].append(rings[i-1])
        print(rod)
        for key in rod:
            if "R" in rod[key] and "G" in rod[key] and "B" in rod[key]:
                print(rod[key])
                ringCounter += 1
        return ringCounter
        