def rightRotate(arr, k):
    n=len(arr)
    ans=[]
    for i in range(0, len(arr)):
        index = (n+i-k)%n
        ans.append(arr[index])

    return ans

def leftRotate(arr, k):
    n = len(arr)
    res = []
    mod = k % n
    for i in range(n):
        idx = (mod + i)%n 
        res.append(arr[idx])

    return res


def reverse(arr, i, j):
    while i<j:
        arr[i],arr[j] = arr[j], arr[i]
        i+=1
        j-=1

def rightRotate2(arr, k):
    n=len(arr)

    reverse(arr, 0, n-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, k-1)

    return arr


def leftRotate2(arr, k):
    n=len(arr)

    reverse(arr, k, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, 0, n-1)

    return arr

ls=[1,2,3,4,5,6,7]
k=2
print("Original: ",ls)
print("Rotated:   ", end="")
res = rightRotate(ls, k)
# res = leftRotate(ls, k)
# res = rightRotate2(ls,k)
# res = leftRotate2(ls, k)
# print(ls)
print(res)


