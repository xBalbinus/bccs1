# O(n) form: how many loops are there? exponentials come in when 
# there are embedded loops.
# Tighter analyses are better! when something is in both O(1) and O(10)
# Choose O(1)

# The sorting function is in O(N log N)

#e.g.

def f(array):
    N = len(array)
    counter = 0
    array = sorted(array)
    for i in range(N):
        for j in range(N):
            counter += 1
    print(counter)
    
# N^2 + N log N = O(N^2)

# O(1) constant
# O(log N) logarithmic
# O(N) linear
# O(N log N) loglinear
# O(N^2) quadratic
# O(N^3) cubic
# O(2^N) exponential

#The better solution to the last quiz.

def sum2(S, A, start):
    count = 0
    left = start
    right = len(A) - 1
    while left < right:
        if A[left] + A[right] == S:
            count += 1
            left += 1
            right -= 1
        elif A[left] + A[right] < 5:
            left += 1
        else:
            right -= 1
    return count
    
    
def sum3(A):
    A = sorted(A)
    N = len(A)
    count = 0
    for i in range(N):
        count += sum2(-A[i], A, i+1)
    return count

def main():
    A = get_input()
    print(sum3(A))
    
''''
   The concept of divide & conquer.
   Look in the middle, split in one half, choose a half to look in, repeat.
   Linear scan vs binary search (binary search is of complexity O(log2(N)), which is much more
   efficient than linear scan)
'''

''''
    Methods of problem solving
    1. Brute Force
    2. Sorting
    3. Reduction
    4. Divide & Conquer
    5. Recursion
'''

#index of an item in a sorted list
def index_of(L, item):
    for i in range(len(L)):
        if L[i] == item:
            return i