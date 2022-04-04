# Tuple implementation of a stack
# Can be confusingly simple
def create(size):
    #Creates an empty tuple
    return ()

def is_empty(stack):
    #Checking whether or not if the tuple is empty.
    return stack == ()

def push(v, stack):
    #Constructing a tuple (v, stack)
    return (v, stack)

def pop(stack): 
    #Returns the value on the top, and the rest of the stack...
    #But because stack was defined recursively, we're done. Just return stack. 
    return stack

#This general recursive structure is what we call a "linked list", where 1 data entry links to the next.




    