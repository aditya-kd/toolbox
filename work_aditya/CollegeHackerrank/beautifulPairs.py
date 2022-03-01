def findPairs(A, B):
    count=0
    for item in A:
        if item in B:
            B.remove(item)
            count+=1
    if count<len(A):
        print(count+1)
    else:
        print(count-1)

arr=[10,11,12,5,14]
arr2=[8,9,11,11,15]
findPairs(arr, arr2)
