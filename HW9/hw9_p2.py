#Given an array of integers A, find the continguous subarray A[i:j] with the largest sum and return its sum.
#Time complexity - O(Nlog(N))

def get_input():
    N = int(input())
    data = [0] * N
    for i in range(N):
        data[i] = int(input())
    return data

data = get_input()

def findBestSubarray(data, left, right):
    if len(data) == 0:
        return 0
    midpoint = (left+right) // 2
    current = bestleftsum = bestrightsum = 0
    for i in range(midpoint - 1, left-1, -1): #From left of midpoint to beginning of array
        current += data[i]
        bestleftsum = max(bestleftsum, current) #Keeps best sum if current sum is less than.
    current = 0 #Reset current sum counter
    for i in range(midpoint + 1, right+1): #From right of midpoint to end of array
        current += data[i]
        bestrightsum = max(bestrightsum, current)
    #Now we look at the combined sum, sum including the middle number
    bestcombinedsum = data[midpoint] + bestleftsum + bestrightsum
    lefthalf = findBestSubarray(data, left, midpoint - 1)
    righthalf = findBestSubarray(data, midpoint + 1, right)
    return max(bestcombinedsum, lefthalf, righthalf)

findBestSubarray(data, 0, len(data)-1)
            