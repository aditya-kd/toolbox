res2=[]
def subsequences2(arr, n, curr=[], index=-1):
    if index== n:
        return
    if len(curr)!=0:
        res2.append(curr)
    for i in range(index+1, n):
        curr.append(arr[i])
        subsequences2(arr,n, curr, i)
        curr= curr[0: len(curr)-1]
    return 

output=[]
arr=[2,-1,2,3,4,-5]
slen=len(arr)
subsequences2(arr, slen)
print(res2)

