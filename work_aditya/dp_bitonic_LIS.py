
def LIS(arr):
    omax=0
    n=len(arr)
    dp=[0]*(len(arr))
    for i in range(n):
        mxm= 0
        for j in range(i):
            if arr[j] < arr[i]:
                if dp[j] >mxm:
                    mxm = dp[j]
        dp[i] = mxm+1
        if dp[i] >omax:
            omax=dp[i]
    print(omax)
    print(dp)

ls=[10,22,9,33,21,50,41,60,80,3]
ls=[21,4,2,16,17,3,13,14]
LIS(ls)

def findCeil(arr, l, r, num):
    while l<r:
        mid= (l+r)//2

        if arr[mid]==num:
            return mid
        elif arr[mid]< num:
            l= mid+1
        else:
            r=mid
    return l

def LISbinarySearch(arr):

    size= len(arr)
    dp=[0 for i in range(size+1)]
    lt=0
    dp[0]=arr[0]
    lt=1
    for i in range(1, size):
        if arr[i] < dp[0]:
            dp[0]= arr[i]
        elif arr[i] > dp[lt-1]:
            dp[lt]= arr[i]
            lt+=1
        else:
            dp[findCeil(dp, -1, lt-1, arr[i])] = arr[i]

    return lt

def lisAgain(arr, n):
    seq=[]
    seq.append(arr[0])
    for i in range(1, n):
        if seq[-1] < arr[i]:
            seq.append(arr[i])
        else:
            ind= findCeil(arr, 0, len(arr), arr[i])
            seq[ind]= arr[i]
    return len(seq)

ls=[10,9,2,5,3,7,101,18]
print(LISbinarySearch(ls))
print(lisAgain(ls, len(ls)))
        