#Problem1
a = int(input())

def getarray(a):
    data = [0] * (a+1)
    for i in range(a+1):
        data[i] = ++i
    return data

data = getarray(a)
print(data)
            
def output(data):
    x = 0
    for i in range(a+1):
        if data[i] % 4 == 0:
            x = x + i
    return(x)
            
output = output(data)
print(output)

    
    