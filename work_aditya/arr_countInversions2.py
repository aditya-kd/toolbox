def getInverts(arr):
    total=0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                total+=1
    return total

def larrysArray(A):
    # Write your code here
    inversions=getInverts(A)
    if inversions%2==0:
        print('YES')
    else:
        print('NO')