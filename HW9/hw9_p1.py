def get_input():
    N = int(input())
    data = [0] * N
    for i in range(N):
        data[i] = int(input())
    return data

data = get_input()

def mergeSort(data):
    #First, split all the numbers up. 
    if len(data) > 1:
        midpoint = len(data) // 2
        leftarray = data[:midpoint]
        rightarray = data[midpoint:]
    #Repeat for each side until each of the arrays reaches 1 in size.
    #This separates each array into a left array, and a right array that splits into another series of left & right arrays.
        mergeSort(leftarray)
        mergeSort(rightarray)
    #After all the numbers are all split up, we try to recombine, from the bottom up.
        i = j = k = 0
        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i] < rightarray[j]:
                data[k] = leftarray[i]
                i += 1
            else:
                data[k] = rightarray[j]
                j += 1
            k += 1
        while i < len(leftarray):
            data[k] = leftarray[i]
            i += 1
            k += 1
        while j < len(rightarray):
            data[k] = rightarray[j]
            j += 1
            k += 1
    return data

x = mergeSort(data)
print(x)