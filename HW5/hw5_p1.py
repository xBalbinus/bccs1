''''

Given a sorted list of integers, compute the smallest difference between two numbers in that list.

Example: consider A = [2, 5, 6, 10]. The output should be 1.

INPUT FORMAT (input arrives from the terminal / stdin):
The first line is a single integer n, the length of the input list.
The next n lines are the contents of the input list.
OUTPUT FORMAT (print output to the terminal / stdout):
Print a single number, the smallest distance.

'''

def get_input():
    n = int(input())
    data = [0] * n
    for i in range(n):
        data[i] = int(input())
    return (data)

input = get_input()

def solution(data):
    data = sorted(data)
    minimum = data[0]
    almostmin = data[1]
    output = almostmin - minimum
    return(output)

x = solution(input)
print(x)