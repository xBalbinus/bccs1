import sys

def get_input():
    s = int(input())
    n = int(input())
    data = [0] * n
    for i in range(n):
        data[i] = int(input())
    return (s, n, data)

#Brute force

def solution(data):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == s:
                count += 1
    return(count)

#Anything you can do with for, you can do with while.
            
solution(data)
print(solution)

#Alternate solutions

def solution(S, data):
    data = sorted(data)
    count = 0
    left = 0
    right = len(data) - 1

    if data[left] + data[right] == S:

        v_left = data[left]
        left_count = 0
        while data[left] == v_left:
            left_count += 1
            left += 1

        v_right = data[right]
        right_count = 0
        while data[right] == v_right:
            right_count += 1
            right -= 1
        
        count += left_count*right_count

    elif data[left] + data[right] < 5:
        left += 1
    else:
        right -= 1

    return count


