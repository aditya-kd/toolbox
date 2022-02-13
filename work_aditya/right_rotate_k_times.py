def rightRotate(arr, k):
    n=len(arr)
    ans=[]
    for i in range(0, len(arr)):
        index = (n-k+i)%n
        ans.append(arr[index])
    print(ans)
    return ans

def reverse(arr, i, j):
    while i<j:
        arr[i],arr[j] = arr[j], arr[i]
        i+=1
        j-=1

def rightRotate2(arr, k):
    n=len(arr)
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    #print list outside. It rotates inplace

ls=[1,2,3,4,5,6,7]
k=2

# rightRotate(ls, k)
rightRotate2(ls,k)
print(ls)


