#file: use max() to recursively find the largest element in a list

#procedure
#   maxoflist
#parameters
#   lst, a list
#produces
#   maximum, a number
#purpose
#   to use basic recursion to find the largest item in a list
#preconditions
#   lst must be entirely numbers that are valid in the max() operator
#   lst must contain at least one element
#postconditions
#   maximum >= x for x in lst

def maxoflist(lst):
    if len(lst) == 1: #if the list is one element (base case)
        return lst[0]
    else:
        return max(lst[0], maxoflist(lst[1:])) #recurse on cdr of lst

#examples

#>>> maxoflist([1, 2, 3, 4, 5])
#5
#>>> maxoflist([1, 2, 3, 4, -5])
#4
#>>> maxoflist([10, 2, 3, 4, 5])
#10
