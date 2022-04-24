from functools import reduce

def read_input():
    M = int(input())
    l = list(map(int,input().split()))
    return (M,l)

def write_output(b):
    print(b)
    
def problem0(l):
    for i in range(1, len(l)-1):
        if l[i-1] > l[i]:
            return False
    return True
def problem1(l):
    for i in range(len(l)-2):
        for j in range(i+1, len(l)-1):
            if l[j] == l[i]:
                return True
    return False
def problem2(l):
    sumofsquares = reduce(lambda x, y: x**2 + y, l, 0)
    sumofbigsq = reduce(lambda x, y: x + y, l, 0)
    if sumofsquares <= sumofbigsq**2:
        return True
    return False
def problem3(l):
    dictionary = {}
    counter = 0
    for i in range(len(l)-1):
        dictionary.setdefault(l[i], counter)
    for i in range(len(l)-1):
        if l[i] in dictionary.keys():
            dictionary[l[i]] += 1
    if dictionary[l[0]] == max(dictionary.values()):
        return True
    else:
        return False
def problem4(l):
    for i in range(len(l)//2):
        if l[i] != l[len(l)-1-i]:
            return False
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