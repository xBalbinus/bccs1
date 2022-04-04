#DATA TYPES NOTES!

#Stack: I have some work that has to be done - will push onto stack and do later.

#Push, pop, create values (or check if empty)

#Data type =/ data structure. Multiple ways to implement data types for real in a data structure.

def match(oc, cc):
    if cc == ')':
        return oc == '('
    elif cc == '}':
        return oc == '{'
    elif cc == ']':
        return oc == '['

def create(size):
    A = [''] * 1
    top = 0
    return (1, top, A)

def push(v, stack):
    (size, top, A) = stack
    if top == size:
        tmp = [''] * (2 * size)
        for i in range(top):
            tmp[i] = A[i]
        A = tmp
    A[top] = v
    top += 1
    return (top, A)

def pop(stack):
    (size, top, A) = stack
    top -= 1
    v = A[top]
    new_stack = (size, top, A)
    return (v, new_stack)

def is_empty(stack):
    (size, top, A) = stack
    return top == 0


def solutions(s):
    
    N = len(s)
    stack = create(N)  

    for i in range(N):
        c = s[i]
        if c == '(' or c == '{' or c == '[':
            stack = push(c, stack)
        else:
            if is_empty(stack):
                return(False)
            (v_top, stack) = pop(stack)
            if not match(v_top,c):
                return False
            
    return is_empty(stack)
    
    #return top == 0

def findMin(nums):
    if len(nums) == 1:
        return nums[0]
    left = 0
    right = len(nums) - 1
    #if rotated 0 times
    if nums[right] > nums[left]:
        return nums[0]
    while right > left:
        mid = (right + left) // 2
        #If mid > mid + 1
        if nums[mid] > nums[mid + 1]:
            return nums[mid+1]
        if nums[mid] < nums[mid-1]:
            return nums[mid]
        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1