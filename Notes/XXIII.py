def s1(l):
    n = []
    for i in range(len(l)):
        n.append(l[i] + 1)
    return n

def s2(l):
    n = []
    for i in range(len(l)):
        n.append(l[i] - 1)
    return n

def s2(l):
    n = []
    for i in range(len(l)):
        n.append(l[i] - 1)
    return n

#You can take a function as a parameter to be put inside another function.
def f(x):
    return x ** 2

def s3(f, l):
    n = []
    for i in range(len(l)):
        n.append(f(l[i]))
    return n

#Different anonymous function types: map, filter, reduce. 
def f(x):
    return x + 1 

lambda x: x + 1
lambda x, y: x + y

l = [1, 2, 3, 4, 5]

def map(f, l):
    n = []
    for i in range(len(l)):
        n.append(f(l[i]))
    return n

map(lambda x: x + 1, l)
list(map(lambda x: x + 1, l))

s = '3 4 2 5 6'
#if you send message split to a string it returns a list containing all of the pieces of the string separated by commas.
l = s.split()

map(int, l)

def map (f, l):
    if l == []:
        return []
    else:
        return [f(l[0])]
    
#Reduce:

def filter(f,l):
    n = []
    for i in range(len(l)):
        print(n,l[i],f(l[i]))
        if f(l[i]):
            n.append(l[i])
    return n

filter(lambda x: x % 2 == 0, [1,2,3,4])

l = [3,6,7,3,4,5,6]

def filter(f, l):
    if l == []:
        return []
    else:
        if f(l[0]):
            return [l[0]] + filter(f, l[1:])
        else:
            return filter(f, l[1:])
        
filter(lambda x: x % 2 == 0, l)

def reduce(f, l, ini):
    acc = ini
    for i in range(len(l)):
        acc = f(acc, l[i])
    return acc

reduce(lambda x, y: x + y, l, 0)

#What if you wanted to multiply?

reduce(lambda x, y: x * y, l, 1 )
        