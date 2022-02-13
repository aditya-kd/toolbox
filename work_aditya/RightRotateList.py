#brute force using nested loops
# def rightRotate1(arr, k, n):
    
#     for j in range(0,k):
#         temp=arr[n-1]
#         for i in range(n-1, 0, -1):
#             arr[i]=arr[i-1]
#         arr[0]=temp
#     print(arr)
#faster appraoc with formula for index
def rightRotate2(arr, k, n):
    ans=[]
    for i in range(0, n):
        index=(n-k+i)%n
        ans.append(arr[index])
    return ans

arr=[1,2,3,4,5]
k=2
n=len(arr)
print(rightRotate2(arr, k, n))