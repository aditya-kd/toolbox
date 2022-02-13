# #brute force
# def rotateLeft(arr, k):
#     for i in range(0,k):
#         temp=arr[0]
#         for j in range(1, len(arr)):
#             arr[j-1]=arr[j]
#         arr[len(arr)-1]=temp
#     return arr

#reverse method
def reverse(arr,s,e):
    beg=s
    end=e
    while(beg<end):
        arr[beg],arr[end]=arr[end],arr[beg]
        beg+=1
        end-=1
    return arr

def leftRotate(arr, k):
    reverse(arr, 0, k-1)
    #print(arr)
    reverse(arr, k, len(arr)-1)
    #print(arr)
    reverse(arr,0,len(arr)-1)
    #print(arr)
    return arr

arr=[1,2,3,4,5]
# #arr=[1,2]
# #arr=[3]
k=2
print(leftRotate(arr, k))


    