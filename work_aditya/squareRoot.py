#Brute Force
def squareRoot(n):
    for i in range(2,n):
        if i**2>n:
            print(i-1)
            break
      
def squreRt(n):
    p=2
    start=1
    end=n
    ans=1
    while start<=end:
        m=(start+end)//2
        if m*m == n:
            print(m)
            return m
        elif m*m < n:
            start=m+1
            ans=m
        else:
            end=m-1

    print(ans)

    return ans
            

# squareRoot(9)
# squareRoot(8)
squreRt(9)

