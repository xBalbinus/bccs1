''''

A relative maximum of an array A is an element of the array that is strictly greater than its neighbors. 
For this purpose, we consider A[-1] = A[len(A)] = - infinity. 
Write an O(log N) program to compute the index of a relative maximum of an input array A.

If A contains multiple relative maximums, print any one of their indices (but just one).

'''

def get_input():
    N = int(input())
    data = [0] * N
    for i in range(N):
        data[i] = int(input())
    return data

array = get_input()

#Binary search but with indices.
def index_of2(L):
    lowlimit = 0
    highlimit = len(L) - 1
    currentpos = ((highlimit + lowlimit) // 2)
    currentitem = L[currentpos]
    while True:
        if currentitem >= L[currentpos-1] and currentitem >= L[currentpos+1]:
            return(currentpos)
        if currentitem < L[currentpos+1]:
            lowlimit = currentpos
            currentpos = ((highlimit + lowlimit) // 2)
            currentitem = L[currentpos]
        if currentitem < L[currentpos-1]:
            highlimit = currentpos
            currentpos = ((highlimit + lowlimit) // 2)
            currentitem = L[currentpos]
            
index_of2(array)
    