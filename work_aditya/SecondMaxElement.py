#Find max element, make it null, now again find the max from
#remaining
# def findSecondMax(arr, n):
#     maxNum=(float('inf'))*-1
#     for i in range(0, n):
#         if arr[i]>maxNum:
#             maxNum=arr[i]
#             largeIndex=i
#     #print(maxNum)
#     maxNum=float('inf')*-1
#     for i in range(0, n):
#         if arr[i]!=arr[largeIndex]:
#             if arr[i]>maxNum:
#                 maxNum=arr[i]
#     # print('second Largest ', maxNum)
#     return maxNum

# #second approach Sorting and find the element at 2nd index
# #from last
# def findSecondMax2(arr, n):
#     arr.sort()
#     temp=arr[-1]
#     i=n-1
#     while(temp==arr[i]):
#         i-=1
#     #print('Second Max: ', arr[i])
#     return arr[i]

#faster method
def findSecondMax3(arr, n):
    inf=float('inf')*-1
    first=inf
    second=inf
    for i in range(0, n):
        if arr[i]>first:
            second=first
            first=arr[i]
        elif arr[i]>second and arr[i]!=first:
            second=arr[i]
    if second!=inf:
        return second
arr=[7,8,56,56,2,4,-1]
n=len(arr)
print(findSecondMax(arr,n))
print(findSecondMax2(arr,n))
print(findSecondMax3(arr,n))



