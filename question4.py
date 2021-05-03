'''
1. Second line is a generator expression and so doesn't construct a
materialised collection. Length of generator expressions, unlike of materialised
collections, is not known. Hence, the expression len(X) causes an error.
2. The function should be a fruitful function which returns a boolean value. The function
as implemented is a non-fruitful function that prints True or False to the user.

 Fix as follows:
'''
def f(L):
    X = [x for x in L for y in L if x+y == 10]
    if(len(X)>0):
        return True
    else:
        return False

