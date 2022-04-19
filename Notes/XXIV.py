from functools import reduce
#Input format on the exam is:
#Given a list of integers, output a boolean value.

def read_input():
    M = int(input())
    l = list(map(int,input().split(" "))) #creates a list of strings
    
(M, l) = read_input()
print(M)
print(l)

def write_output(bool):
    print(bool)
    
def problem0(l):
    #for i in l:
    #   if i%2 != 0:
    #        return False
    #return True
    l = list(filter(lambda v: v % 2 != 0, l))
    return len(l) == 0
    
def problem1(l):
    ''''
    acc = 0
    for v in l:
        acc = acc + v
    return acc % 2 == 0
    '''
    s = reduce(lambda acc, v: acc + v, l, 0)
    return s % 2 == 0

def problem2(l):
    S = set()
    for v in l:
        S.add(v)
    return len(S) % 2 == 0
    
def dispatch(M, l):
    if M == 0:
        bool = problem0(l)
        return bool
    elif M == 1:
        bool = problem1(l)
        return bool
    elif M == 2:
        bool = problem2(l)
        return bool
    
(M, l) = read_input()
bool = dispatch(M, l)
write_output(bool)
    
        
    