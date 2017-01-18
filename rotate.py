# rotating matrix clockwise

# returns list of lists

def rotate(matrix):
    if matrix is None or len(matrix)<1:
        return
    else:
        if len(matrix)==1:
            return matrix
        else:
            # solution matrix
            soln = [row[:] for row in matrix]
            # size of matrix
            m = len(matrix[0])
                    
            for x in range(0,m):
                for j in range(0,m):
                    # print matrix[x][j]
                    # print soln[j][m-1-x]
                    soln[j][m-1-x] = matrix[x][j]
            return soln

six = [["a","b","c"],
          [1,2,3],
          ["x","y","z"]]

print rotate(six)




# or this way - returns list of tuples

def rotate1(matrix):
    return zip(*matrix[::-1])

print rotate1(six)