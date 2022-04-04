def get_input():
    n = int(input())
    data = [0] * n
    for i in range(n):
        data[i] = int(input())
    return (data)

data = get_input()

#Count the number of triples in the array that sum to 0.
#Do you need only the negative and positive version of the same number + 0?
def solution(array):
    counter = 0
    for i in range(len(array)-1):
            for j in range(i+2, len(array)-1):
                if data[i] + data[j-1] + data[j] == 0:
                    counter += 1
    return(counter)
solution(data)