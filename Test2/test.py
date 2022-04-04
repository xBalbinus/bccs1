''''
Input file
line 1 - integer M
line 2 - integer N
following N lines are the decimal values

M = 1 print (D) sorted
M = 2 print mean
M = 3 sample variance
M = 4 print (sample median)
M = 5 print max
M = 6 print Min
else print "unknown command
N = 0 "no data"
'''

m = int(input())
n = int(input())

def get_input(n):
    data = [0] * n
    for i in range(n):
        data[i] = float(input())
    return (data)

data = get_input(n)

def solution(m, n, data):
    if n == 0:
        return("No data")
    elif m == 0:
        print(data)
    elif m == 1:
        data = sorted(data)
        print(data)
    elif m == 2:
        total = 0
        for i in range(len(data)):
            total = total + data[i]
        mean = total / (len(data))
        print(mean)
    elif m == 3:
        total = 0
        numerator = 0
        for i in range(len(data)):
            total = total + data[i]
        mean = total / (len(data))
        denominator = len(data) - 1 
        for i in range(len(data)):
            numerator = (data[i]-mean)**2 + numerator
        variance = numerator / denominator
        print(variance)
    elif m == 4:
        if type(len(data)/2) == int:
            median = ((data[len(data)/2] + data[len(data)/2 + 1]))/2
            print(median)
        else:
            for i in range(len(data)):
                if i-1 == (len(data)-i):
                    print(data[i])
    elif m == 5:
        data = sorted(data)
        print(data[len(data)-1])
    elif m == 6:
        data = sorted(data)
        print(data[0])
    else:
        print("Unknown command")

solution(m, n, data)