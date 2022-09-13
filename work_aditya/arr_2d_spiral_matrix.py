def solve(n):

    value = 1
    m = n
    mn = m*n
    state =[0,0,0]

    result=[[0]*n]*m
    top = 0
    bottom = m-1
    left = 0
    right = n-1
    while value <= mn:
        i = state[0]
        j = state[1]
        d = state[2]

        result[i][j] = value
        value+=1

        if d==0:
            j+=1
            if j>right:
                j-=1
                d = (d+1)%4
                i+=1
                top+=1

        elif d==1:
            i+=1
            if i > bottom:
                i-=1
                d = (d+1)%4
                j-=1
                right -=1

        elif d==2:
            j-=1
            if j<left:
                j+=1
                d=(d+1)%4
                i-=1
                bottom-=1

        elif d==3:
            i-=1
            if i<top:
                i+=1
                d=(d+1)%4
                j+=1
                left+=1

        state = (i,j,d)

    return result




