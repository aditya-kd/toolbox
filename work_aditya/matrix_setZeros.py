def setZeros(matrix):
    rows= len(matrix)
    cols = len(matrix[0])

    flag=False
    #finding which rows/cols need to be zero
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r>0:
                    matrix[r][0] = 0
                else:
                    flag=True
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[0][c] ==0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] =0 
    if flag==True:#meas first row needs to be zero
        for c in range(cols):
            matrix[0][c]=0

    print (matrix)



