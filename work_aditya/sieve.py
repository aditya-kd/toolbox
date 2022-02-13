import math
def seive():
    n=20**3
    arr=[True for i in range(20**3)]
    arr[0]=False
    arr[1]=False
    for i in range(2, (n)):
        if arr[i]==True:
            for j in range(i*i, n+1, i):
                arr[j]=False
    total=0
    num=2
    res=[]
    while total!=1200:
        if arr[num]==True:
            res.append(num)
        total+=1
        num+=1
    
    print(arr[n])
#seive for a range
def seiveRange(n):
    if n==0:return 0
    if n==1:return 0
    arr=[True for i in range(10**7)]
    arr[0]=False
    arr[1]=False
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i]==True:
            for j in range(2*i, n+1, i):
                arr[j]=False
    c=0
    for i in range(2,n):
        if arr[i]==True:
            # print(i, arr[i])
            c+=1
    print('Prime Numbers less than',n,'=',c)
    return c
def seive3(n):
    seen, ans = [0] * (n+1), 0
    for num in range(2, n):
            if seen[num]: continue
            ans += 1
            seen[num*num:n:num] = [1] * ((n -1)// num - num + 1)
    return ans


print('Length of seive')
print(len(seive()))
    
# seiveRange(10)