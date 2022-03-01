# import sys
# def solve(arr,k):
#     k-=1
#     arr.sort()
#     ans=sys.maxsize
#     for i in range(len(arr)-k):
#         if ans> arr[i+k]-arr[i]:
#             ans=arr[i+k]-arr[i]
#     return ans
import sys
def solve(arr,k):
    k-=1
    arr.sort()
    ans=sys.maxsize
    for i in range(len(arr)-k):
        j=i+k#end 
        if ans> arr[j]-arr[i]:
            ans=arr[j]-arr[i]
    return ans


k=2
arr=[1,4,7,2]
print(solve(arr, k))
