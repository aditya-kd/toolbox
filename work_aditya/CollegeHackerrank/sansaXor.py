def sansaXor(arr):
    n=len(arr)
    ans=0
    for i in range(n):
        total_ways=(i+1)*(n-1)
        if total_ways%2!=0:
            ans=ans^arr[i]

    return ans

