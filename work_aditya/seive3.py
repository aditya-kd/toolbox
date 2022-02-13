import math
def seiveRange(n):
    if n==0:return 0
    if n==1:return 0
    n=10**7
    arr=[True for i in range(10**7 +1)]
    arr[0]=False
    arr[1]=False
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i]==True:
            for j in range(2*i, n+1, i):
                arr[j]=False
    # print(arr)
    c=1200
    res=[]
    i=0
    while c>0:
        if arr[i]==True:
            res.append(i)
            c-=1
        i+=1
    return res


print(seiveRange(1200))