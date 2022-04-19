l = [2, 5, 42, 6, 7, 3, 4]
#Returns all entries up to n-1 (e.g. l[:2] returns l[0] and l[1])
l[:2]

#Normal iterative
def lsum1(l):
    acc = 0
    for i in range(len(l)):
        acc += l[i]
    return acc
lsum1(l)

#Recursive solution. O(Nlog(N))
def lsum2(l):
    if l == []:
        return 0
    else:
        v = l[0]
        subproblem = l[1:]
        solved_subproblem = lsum2(subproblem)
        solution_for_complete_problem = v + solved_subproblem
        return solution_for_complete_problem

lsum2(l)

#Insertion sort recursively.
def insertion(v, l):
    if l == []:
        return [v]
    elif l[0] >= v:
        return [v] + l
    else:
        return l[:1] + insertion(v, l[1:])
    
insertion(4, [1,2,5,6])

def insertionSort(l):
    if len(l) <= 1:
        return l
    else:
        #divide 
        v = l[0]
        subproblem = l[1:]
        # "magic"  
        solved_subproblem = insertionSort(subproblem)
        solution_to_overall_problem = insertion(v, solved_subproblem)
        #done
        return solution_to_overall_problem

#driver code for insertionSort
l = [4,2,4,6,7,3,4]
insertionSort(l)