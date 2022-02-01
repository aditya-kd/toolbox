def nger(arr):
    n=len(arr)-1
    ls=[-1]*(n+1) #if we declare it like this, we won't need to reverse it.
    s=[]

    for i in range(len(arr)-1, -1, -1):

        while len(s)>0 and s[-1]<= arr[i]:
            s.pop()

        if len(s)==0:
            ls[n]=-1
            n-=1
            # ls.append(-1)
        else:
            ls[n]=s[-1]
            n-=1
        
            # ls.append(s[-1])

        s.append(arr[i])
    print(ls)
    return ls

ls=[10, 7, 5, 4, 9, 2, 1]
ls=[4,5,7,8,2,6]

nger(ls)

    