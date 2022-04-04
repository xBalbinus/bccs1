#Problem solving framework:
#1. Subdivide problems
#2. Assume Problem Solved
#3. Recombine problems

#Example: insertion sort

ex1 = [8,1,2,3,4,5,6,7]
ex2 = [4,1,2,3,5,6,7,8]
ex3 = [5,1,2,3,4,6,7,8]

def insert(array):
        for i in range(1, len(array)):
            key = array[i]
            j = i-1
            while j >= 0 and key <= array[j]:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
        return(array)

insert(ex3)
#Time complexity: O(N^2)
