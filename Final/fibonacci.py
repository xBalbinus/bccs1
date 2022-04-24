#https://leetcode.com/problems/fibonacci-number/submissions/

class Solution:
    def fib(self, n: int) -> int:
        fList = []
        fList.append(0)
        fList.append(1)
        for i in range(1, n):
            next = fList[i-1] + fList[i]
            fList.append(next)
            print(fList)
        return fList[n]