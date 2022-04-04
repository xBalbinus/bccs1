def get_input():
    data = [0] * 7
    for i in range(7):
        data[i] = int(input())
    return data

data = get_input()

def solution(data):
    data = sorted(data)
    x = data[0]
    y = data[1]
    largest_value = [data(len(data) - 1)]
    z = largest_value - (x+y)
    return(x,y,z)

result = solution(data)

