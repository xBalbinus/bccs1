''''

Implement binary search. Your program will accept a sorted array of distinct integers A and an integer x, and should print the index of x if it lies in A, or -1 if the value does not exist in the list.

As you are implementing binary search, your solution must be in O(Log N). Slower solutions will be marked as incorrect.

'''

def get_input():
    N = int(input())
    data = [0] * N
    for i in range(N):
        data[i] = int(input())
    return data

item = int(input())
L = get_input()

#Implementation of binary search
def index_of2(item, L):
    lowlimit = 0
    highlimit = len(L) - 1
    currentpos = ((highlimit + lowlimit) // 2)
    currentitem = L[currentpos]
    while True:
        if currentitem == item:
            return(currentpos)
        if currentitem < item:
            lowlimit = currentpos
            currentpos = ((highlimit + lowlimit) // 2)
            currentitem = L[currentpos]
        if lowlimit == currentpos or highlimit == currentpos and currentitem != item:
            return(-1)
        if currentitem > item:
            highlimit = currentpos
            currentpos = ((highlimit + lowlimit) // 2)
            currentitem = L[currentpos]
            
index_of2(item, L)

#Time complexity: O(Nlog(N))