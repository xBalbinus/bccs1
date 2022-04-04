''''
Given the number of stalls and a list of occupied stall numbers, find the stall to put the new horse in. 
If there are several stalls that the new horse can be placed in, 
then the horse will be placed in the stall closest to the end (i.e. the largest stall number).

Example: consider num_stalls = 10, occupied_stalls = [1, 2, 8]. The output should be 5.

'''

num_stalls = int(input())

def get_input():
    n = int(input())
    data = [0] * n
    for i in range(n):
        data[i] = int(input())
    return (data)

occupied_stalls = get_input()

def largestSpace(occupied_stalls, num_stalls):
    occupied_stalls = sorted(occupied_stalls)
    #Current number with largest distance
    currentLargest = 0
    #Current shortest distance counter
    currentdistanceCounter = 0
    newdistanceCounter = 0
    for i in range(1, num_stalls+1):
        for j in range(1, len(occupied_stalls)):
            #Selecting range for distance comparison
            if i >= occupied_stalls[j-1] and i <= occupied_stalls[j]:
                #calculate distance to each endpoint
                if (i - occupied_stalls[j-1]) > abs(i - occupied_stalls[j]):
                    newdistanceCounter = abs(i - occupied_stalls[j])
                    #set currentLargest to one with the largest newDistance.  
                    #set currentDistance to newdistance.
                    if currentdistanceCounter <= newdistanceCounter:
                        currentLargest = i
                        currentdistanceCounter = newdistanceCounter
                elif i - occupied_stalls[j-1] < abs(i - occupied_stalls[j]):
                    newdistanceCounter = i - occupied_stalls[j-1]
                    if currentdistanceCounter <= newdistanceCounter:
                        currentLargest = i
                        currentdistanceCounter = newdistanceCounter
                elif i - occupied_stalls[j-1] == abs(i - occupied_stalls[j]):
                    newdistanceCounter = i - occupied_stalls[j-1]
                    if currentdistanceCounter <= newdistanceCounter:
                        currentLargest = i
                        currentdistanceCounter = newdistanceCounter
        if i > occupied_stalls[len(occupied_stalls) - 1] and i <= num_stalls:
            #set newdistance to counter against max of list
            newdistanceCounter = (i - occupied_stalls[len(occupied_stalls) - 1])
            if currentdistanceCounter <= newdistanceCounter:
                currentLargest = i
                currentdistanceCounter = newdistanceCounter
    return(currentLargest)

answer = largestSpace(occupied_stalls, num_stalls)
print(answer)