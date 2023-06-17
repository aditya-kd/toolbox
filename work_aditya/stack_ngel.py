def ngel(arr):
    n=len(arr)-1
    ls=[-1]*(n+1)
    s=[]
    index=0

    for i in range(0, len(arr)):

        while len(s)>0 and s[-1] <= arr[i]:
            s.pop()

        if len(s)==0:
            ls[index]=-1
            index += 1
        #   ls.append(-1)
        else:
            ls[index] = s[-1] 
            index += 1

        s.append(arr[i])

    print(ls)
    return ls

ls=[4,3,9,5,6,2,7]
ngel(ls)
