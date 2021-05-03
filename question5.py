def number_of_differences(n, m, A, B):
    count = 0
    for i in range(0,n):
        for j in range(0,m):
            if A[i][j] != B[i][j]:
				count+=1
    return count

assert number_of_differences(2,3, [[1,2,3], [4,5,6]], [[1,2,4],[3,5,6]]) == 2
assert number_of_differences(2,2, [[1,2], [3,4]], [[1,2], [3,4]])== 0