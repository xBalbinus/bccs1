''''
Implement insertion sort. 
Given an array of integers A and an integer x = 0, 
sort A from low to high if x = 0 and high to low if x = 1.
'''
ordering = int(input())

def get_input():
    N = int(input())
    data = [0] * N
    for i in range(N):
        data[i] = int(input())
    return data

data = get_input()

def insertionsort(ordering, array):
    if ordering == 1:
        for i in range(1, len(array)):
            key = array[i]
            j = i-1
            while j >= 0 and key >= array[j]:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
    if ordering == 0:
        for i in range(1, len(array)): 
            key = array[i]
            j = i-1 #Iterate from 1 to end of array + 1 for key
            while j >= 0 and key <= array[j]:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
    for i in range(len(array)):
        print(array[i])

insertionsort(ordering, data)