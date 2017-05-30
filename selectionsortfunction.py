#file: Use recursion to sort a lst by a binary predicate

#citations: code and documentation based on vector-selection-sort! from csc151 exam 4, availible http://www.cs.grinnell.edu/~rebelsky/Courses/CSC151/2017S/exams/exam4.html

#procedure
#   selectionsort
#parameters
#   lst, a list
#   pred, a binary predicate
#purpose
#   to sort a list based on a binary predicate
#produces
#   sortedlst, a list
#preconditions
#   all elements of lst must be valid inputs to pred
#   lst must contain at least two elements
#postconditions
#   element 0 of sortedlst will fail the binary predicate against element 1, and so on

def selectionsort(lst, pred):
    def mostpred(lst): #finds most extreme value
        if len(lst) == 1: #base case
            return lst[0]
        else:
            return pred(lst[0], mostpred(lst[1:])) #recurse of cdr of lst
    def selectionsorthelper(lst, result):
        if not lst: #base case
            return result
        else:
            return selectionsorthelper(lst[:lst.index(mostpred(lst))] + lst[lst.index(mostpred(lst))+1:], result + [mostpred(lst)])
    return selectionsorthelper(lst, [])


#note that this relies on multiple standard recursions and would not scale to extremely large lists


#examples

#>>> selectionsort([1, 2, 5, 3, 4], max)
#[5, 4, 3, 2, 1]
#>>> selectionsort([1, 2, 5, 3, 4], min)
#[1, 2, 3, 4, 5]
#>>> selectionsort([1, 2, 5, 3, 4, 5], max)
#[5, 5, 4, 3, 2, 1]
#>>> selectionsort([2,5,2,4,23,8,5,3,45,6,5,5,4,4,6,6,45,4,3,9,6], min)
#[2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 8, 9, 23, 45, 45]
