class Solution:
    def countPoints(self, rings: str) -> int:
        
        rods = {}
        for i in range(10):
            rods[i] = set()
        
        N = len(rings) // 2
        for i in range(N):
            color = rings[2*i]
            rod = int(rings[2*i + 1])
            rods[rod].add(color)
            
        count = 0
        for i in range(10):
            if len(rods[i]) == 3:
                    count += 1
                    
        return count
    

# Cross-functional calls
# What happened:
# At the top level of the program / defining functions & classes
# function H has its own environment to keep track of its variables
# Calling each function has its own environment (h, g, f all have their own states)

def f(x):
    if x == 3:
        return 42
    else:
        y = x + 1
        return y

