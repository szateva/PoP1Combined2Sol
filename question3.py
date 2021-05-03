'''
The given implementation of add_row adds to the matrix A n references to the
same instance of v. Hence when we change the value of v,
we change the content of all elements that we added to the matrix because they
reference it. Fix using copy() method:
'''
def add_row(A,v,n):
    for i in range(n):
        A.append(v.copy())

