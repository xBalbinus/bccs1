import math

def get_input():
    N = int(input())
    data = [0] * N
    for i in range(N):
        data[i] = int(input())
    return data

#Implementation of binary search
def index_of2(L, item):
    L = sorted(L)
    lowlimit = 0
    highlimit = len(L) - 1
    currentpos = math.floor(highlimit + lowlimit / 2)
    currentitem = L[currentpos]
    while True:
        if currentitem == item:
            return(currentpos)
        if currentitem <= item:
            lowlimit = currentpos
        else:
            highlimit = currentpos

    
#L = get_input()
#index_of2(L, 3)
#Time complexity: O(logbase2(N))