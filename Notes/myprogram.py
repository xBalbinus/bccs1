import sys

M = float(input())
X = float(input())
Y = float(input())

def solution(M, X, Y):
   
    if (M == 0):
        print(X+Y)
    elif (M == 1):
        print(X-Y)
    else:
        print("42")

answer = solution(M, X, Y)
print(answer)



    


