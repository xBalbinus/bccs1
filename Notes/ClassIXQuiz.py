def get_input():
    # When you call input, remember not to pass a string as an argument
    # input() --> Good
    # input('Enter a number') --> NOT good
    x = int(input())
    y = int(input())
    return (x,y)

def solution(x,y):
    if x >= y:
        return x
    else:
        return y
    
# You need to call the functions you just defined if you want something to happen!    
(x,y) = get_input()
result = solution(x,y)

# Print the result as described in the output specification, and nothing else
print(result)