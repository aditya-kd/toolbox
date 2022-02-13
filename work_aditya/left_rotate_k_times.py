def leftRotate(arr, k):
    ans=[]
    n=len(arr)
    mod= k%n
    for i in range(n):
        # print(arr[(mod+i)%n], end="")
        ans.append(arr[(mod+i)%n])
    print(ans)
    return ans

def reverse(arr, i, j):
    while i<j:
        arr[i], arr[j]= arr[j],arr[i]
        i+=1
        j-=1
def leftRotate2(arr, k):
    n=len(arr)
    reverse(arr, 0, n-1)
    reverse(arr, 0, n-k-1)
    reverse(arr, n-k, n-1)
    #print outside
    
ls=[1,2,3,4,5]
k=3
# leftRotate(ls, k)
leftRotate2(ls, k)
print(ls)
