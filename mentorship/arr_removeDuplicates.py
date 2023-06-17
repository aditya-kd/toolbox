# O(N) Space
def removeDuplicate1(arr, n):
        
    res = []
    res.append(arr[0])
    for i in range(1, n):
        if arr[i-1] != arr[i]:
            res.append(arr[i])

    return res

# O(1) Space
def removeDuplicates(arr, n):
    res = [0]*n
    k = 1
    for i in range(1, n):
        if arr[i-1] != arr[i]:
            arr[k] = arr[i]
            k+=1 
    
    for i in range(0, k):
        print(arr[i], end=" ")


ls = [1,1,2,3,4,4,4,5, 5,5]
# ls = [1,5,3,4,5,2,5]
n = len(ls)

# removeDuplicates(ls, n)
print(removeDuplicate1(ls, n))





