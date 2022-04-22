from functools import reduce

def read_input():
    M = int(input())
    l = list(map(int,input().split()))
    return (M,l)
def write_output(b):
    print(b)
def problem0(l):
    return True
def problem1(l):
    return True
def problem2(l):
    return True
def problem3(l):
    return True
def problem4(l):
    return True
    
def dispatch(M,l):
    if M == 0:
        b = problem0(l)
        return b
    elif M == 1:
        b = problem1(l)
        return b
    elif M == 2:
        b = problem2(l)
        return b
    elif M == 3:
        b = problem3(l)
        return b
    elif M == 4:
        b = problem4(l)
        return b
    
(M,l) = read_input()
b = dispatch(M,l)
write_output(b)