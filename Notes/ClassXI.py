import sys

#A function with no input
def f0():
    counter = 0
    counter += 1
    counter += 1
    counter += 1
    counter += 1
    counter += 1
    counter += 1
    print(counter)
    
f0()
        
def f1(N):
    counter = 0
    for i in range(N):
        counter += 1
    print(counter)
    
f1(100)

#Python has execution times that adds up for each function.
#If a bunch of statements follow each other, you can sum up the approximate time it takes to run each.

def f3(N):
    counter = 0
    for i in range(N):
        counter += 1
    for j in range(N):
        counter += 1
    print(counter)

#Should output 2N
f3(100)

def f5(N):
    counter = 0
    for i in range(N):
        for j in range(i+1, N):
            counter += 1
    print(counter)
    
f5(100)