
def get_input():
    n = int(input())
    data = [0] * n
    for i in range(n):
        data[i] = int(input())
    return (data)

input1 = get_input()
input2 = get_input()
mergedlist = input1 + input2
    
def solution(mergedlist):
    anslist = sorted(mergedlist)
    print(anslist)

solution(mergedlist)
