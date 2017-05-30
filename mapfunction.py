#file: re-write python "map" function by hand

#procedure
#   mymap
#parameters
#   fuction, a function of one parameter (expressed by lambda)
#   lst, a list
#produces
#   mappedlst, a list
#purpose
#   to apply function to each element of lst
#preconditions
#   elements of lst must be valid parameters to function
#postcontitions
#   elements of mapped-lst will be in the same order as lst
#   python standard map(function, lst) will return the same as mymap(function, lst)

def mymap(function, lst):
    def mymaphelp(lst, result): #add result parameter
        if not lst: #if the list is empty (base case)
            return result
        else:
            return mymaphelp(lst[1:], result + [(function(lst[0]))]) #call the function recursively on a "cdr" of the list
    return mymaphelp(lst, [])


#examples

#map
    
#test-funtion: lambda x: x**2
#test-lst = [1, 2, 2.5, 10, -1, 0]

#>>> lst = [1, 2, 2.5, 10, -1, 0]
#>>> squared = list(map(lambda x: x**2, lst))
#>>> print(squared)
#[1, 4, 6.25, 100, 1, 0]

#mymap
#>>> mymap(lambda x: x**2, [1, 2, 2.5, 10, -1, 0])
#[1, 4, 6.25, 100, 1, 0]
