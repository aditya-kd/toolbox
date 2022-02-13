def sumList(arr):
    sum=0
    n=len(arr)
    for i in range(0,n):
        sum+=arr[i]
    return sum
def maxSumSublist(arr):
    n=len(arr)
    sum=0
    maxList=[]
    for i in range(0, n):
        for j in range(i+1, n+1):
            curlist=[]
            for k in range(i, j):
                curlist.append(arr[k])
            curSum=sumList(curlist)
            if curSum>sum:
                sum=curSum
                maxList=curlist
            print('Curlist: s=',i,' e=',j,' ',curlist)
    print(maxList)

#faster approach using kadanes algorithm
def maxSumSublist2(arr):
    csum=arr[0]
    osum=arr[0]
    start=0
    end=0
    curList=[]
    for i in range(0, len(arr)):
        if csum>=0:
            csum+=arr[i]
            end=i
        else:
            csum=arr[i]
            start=i
        if osum<csum:
            osum=csum
    for i in range(start, end+1):
        curList.append(arr[i])
    return curList

arr=[-89,34,5,2,3,4,1,22]
arr=[1,4,2]
arr=[1,100,4,3,101,6,5]
arr.sort()
maxSumSublist(arr)
print('Second Function')
print(maxSumSublist2(arr))

            

