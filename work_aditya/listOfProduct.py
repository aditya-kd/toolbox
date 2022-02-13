# #Brtue Force finding product everytime except the number itself
# def listofProduct(arr,n):
#     res=[1]*n
#     for i in range(0, n):
#         prod=1
#         for j in range(0, n):
#             if j!=i:
#                 prod*= arr[j]
#         res[i]=prod
#     #copy back to original array
#     arr=[]
#     for i in range(0, n):
#         arr.append(res[i])
#     return arr

#faster approach find product of all at once then divide by
#each number at the position
def findProdcut(arr, n):
    prod=1
    for i in arr:
        prod*= i
    for i in range(0, n):
        arr[i]=prod//arr[i]
    return arr
arr=[7,8,5,6,2]
n=len(arr)
# print(listofProduct(arr, n))
print(findProdcut(arr,n))

        
            