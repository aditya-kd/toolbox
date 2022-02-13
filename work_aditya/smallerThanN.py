# def findSmaller(arr, n):
#     s=0
#     e=len(arr)-1
#     while s<=e:
#         m=(s+e)//2
#         if arr[m]==n:
#             e=m-1
#         elif arr[m]>n:
#             e=m-1
#         else:
#             s=m+1
#     print(arr[m])



def findFirstOccurrence2(arr, n, target):
    start=0
    end=n-1
    ans=0
    while(start<=end):
        m=(start+end)//2
        if arr[m]==target:
            ans=m
            end=m-1
        elif arr[m]>target:
            end=m-1
        else:
            start=m+1
    return ans

arr=[1,2,2,3,4]
print(findFirstOccurrence2(arr, len(arr), 3))
print('THis is the firs tcark')



