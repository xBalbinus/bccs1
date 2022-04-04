''''

You are given a command M and an array of integers D. D is of size N.
Your goal is to do the following:
•If M is 0, then you should print the values of D, by increasing order of index, one per
line;
•If M is 1, then you should print the string ’Palindrome’ if the array is a palindrom and
’Boring’ otherwise.
An array is a palindrome if its values read the same forward and backward.

The input file contains 1 integer per line.
•Line 1 is M;
•Line 2 is N;
•The following N lines are the values D[0], D[1], ···, D[N −1].

'''

m = int(input())

def get_input():
    n = int(input())
    data = [0] * n
    for i in range(n):
        data[i] = int(input())
    return (data)

dArray = get_input()

def solution(m, dArray): 
    if m == 0:
        dArray = sorted(dArray)
        print(dArray)
    elif m == 1:
        i = 0
        while i < (len(dArray)//2):
            if dArray[i] != dArray[(len(dArray) - 1 - i)]: #@audit -1 to keep in range
                i += 1
                return("Boring")
            else:
                return("Palindrome")

solution(m, dArray)