#insertion sort
def binarySrch(arr, key, start, end):
    while start<end:

        mid= (start+end)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            end=mid-1
        else:
            start=mid+1
    return start

def printMedian(arr, n):
    count=1
    #first element always zero
    for i in range(1, n):
        median=0
        j=i-1
        num=arr[i]
        pos = binarySrch(arr, num,0, j)
        while j>=pos:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=num
        count+=1
        if count%2 !=0:
            median = arr[count//2]
        else:
            median = (arr[(count//2)-1] + arr[count//2])/2
        print(median)

arr=[5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
n=len(arr)
printMedian(arr, n)
