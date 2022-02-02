#maximum sum subarray of size k
def maxSumSubArrK(arr, n, k):
    cursum=0
    maxsum=-1
    i=0
    j=0
    while j<n:

        cursum+= arr[j]
        if j-i+1 <k:            
            j+=1
        
        elif j-i+1 == k:
            maxsum = max(cursum, maxsum)
            cursum-=arr[i]
            i+=1
            j+=1
        

    print(maxsum)


ls=[1,0,-1,3]
k=3
maxSumSubArrK(ls, len(ls), k)
            