#Given a list of integers, separate the odd and even numbers in it into two separate lists.

def get_input():
    n = int(input())
    data = [0] * n
    for i in range(n):
        data[i] = int(input())
    return (data)

input = get_input()

def solution():
    evenList = []  #list for storing even number
    oddList = [] #list for storing odd number
    for j in input:
        if j%2==0:
            evenList.append(j)
        else:
            oddList.append(j)
    print(oddList)
    print(evenList)

solution()