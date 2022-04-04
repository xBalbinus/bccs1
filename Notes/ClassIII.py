import math

def solver(a, b, c):
    if not (ct(a) and ct(b) and ct(c)):
        raise ValueError('One of the arguments is of wrong type')
    if a == 0:
        raise ValueError('a should not be equal to 0!')
        return
    tmp = b**2 - 4 * a * c
    if tmp < 0:
        raise ValueError('no real solutions')
        return
    sr = math.sqrt(tmp)
    d = 2 * a
    if tmp == 0:
        print('only one solution', -b/d)
    else:
        x1 = (-b + sr) / d
        x2 = (-b - sr) / d
    print("First solution: ", x1)
    print("Second solution: ", x2)
    return(a * x1 ** 2 + b * x2 + c)



def ct(x):
    return type(x) == int or type(x) == float

result = solver(1, 4, 2)

ct(4.5)
ct(True)
ct((3,4))



print(result)

'''
or
'''

def test(x):
    result = x+1
    return result

test(43)

x1 = 2
x2 = "lemon"

x = (x1, x2)

print(x)

x[0]

#You can write both numbers or strings inside a tuple.



#nested tuples

y1 = 3
y2 = 40
y3 = (1, "orange", 5)

y = (y1, y2, y3)

print(y)

y[2][1]


def solver_sum(a, b, c):
    (x1, x2) = solver(a, b, c)
    print (x1 + x2)


#round outputs an integer
round(4.4)

# this rounds down to 4! 
round(4.5) 

type(round(4.4))

math.floor(4.7)
math.ceil(4.3)

type(y)

#coerces to int
type(int(z))

#booleans = true / false