#Problem2a = int(input())def get_input(x):    data = [0] * x    for i in range(x):        data[i] = int(input())    return datadata1 = get_input(a)b = int(input())data2 = get_input(b)print(data1)print(data2)    def mult(data1, data2):    x = 0    for i in range(len(data1)):        for j in range(len(data2)):            x = x + data1[i] * data2[j]    return(x)answer = mult(data1, data2)print(answer)