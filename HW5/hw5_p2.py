''''
Given a list of integers, make a new list of the cumulative sums of preceding numbers at each index.

Example: consider A = [2, 4, -1]. The output should be [2, 6, 5].

INPUT FORMAT (input arrives from the terminal / stdin):
The first line is a single integer n, the length of the input list
The next n lines are the contents of the input list.
OUTPUT FORMAT (print output to the terminal / stdout):
Print the cumulative list.
'''

def get_input():
    n = int(input())
    data = [0] * n
    for i in range(n):
        data[i] = int(input())
    return (data)

input = get_input()

def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]

answer = Cumulative(input)
print(answer)