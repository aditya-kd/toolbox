def sortedMinMax(arr):
    great=[]
    small=[]
    n=len(arr)
    for i in range(n, n//2, -1):
        great.append(arr[i])
    for i in range(n//2, -1, -1):
        small.append(arr[i])
    print(great, small)
    i,j=0,0
    n1=len(great)
    n2=len(small)
    res=[]
    flag=True
    while i<n1 or j<n2:
        if i<n1 and flag==True:
            res.append(great[i])
            i+=1
            flag=False
        elif j<n2 and flag==False:
            res.append(small[j])
            j+=1
            flag=True
            


def sortedMinMax2(arr):
    start=0
    end=len(arr)-1
    res=[]
    while(start<end):
        res.append(arr[end])
        res.append(arr[start])
        start+=1
        end-=1


    print(res)   


arr=[7,8,5,6,2,-1]
arr.sort()
sortedMinMax2(arr)

    