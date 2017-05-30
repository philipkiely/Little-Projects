#file: use basic recursion to compute the sum of a list

#procedure
#   sumoflist
#parameters
#   lst, a list
#produces
#   sum, a number
#purpose
#   to use basic recursion to find the largest item in a list
#preconditions
#   lst must be entirely numbers that are valid in the + operator
#   lst must contain at least one element
#postconditions
#   sum = x1 + x2 + ... + xn for lst of length n

def sumoflist(lst):
    if len(lst) == 1: #if the list is one element (base case)
        return lst[0]
    else:
        return lst[0] + sumoflist(lst[1:]) #recurse on cdr of lst

    
#examples
#>>> sumoflist([1, 2, 3, 4, -5])
#5
