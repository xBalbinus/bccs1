#The way we came up with insertion sort is DIVIDE & CONQUER.
#First, divide your bigger problems into subproblems
#Assume the problem is solved
#Conquer: Construct solution to sub problems
#Re-merge the smaller problems into the bigger problem.


A1 = [1,3,5,12]
B1 = [2,7,23]

def merge(A,B):
    N = len(A)
    M = len(B)
    C = [0] * (N+M)
    
    i = 0
    j = 0
    k = 0
    
    while i < N and j < M:
        if A[i] < B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1

    if i == N:
        while j < M:
            C[k] = B[j]
            j += 1
            k += 1
    else:
        while i < N:
            C[k] = A[i]
            i += 1
            k += 1
        
    return C

print(merge(A1, B1))
        
#Time complexity: O(N log N)