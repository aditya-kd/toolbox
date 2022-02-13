#Brute Force but not O(logn)
def shiftedArrMin(arr, n):
    arr.sort()
    min=float('inf')
    for i in range(n):
        if min>arr[i]:
            min=arr[i]
    return min

#
def shiftedMinAr(arr, n):
    #find the breakpoint
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            print('Breakpoint', i)
            breakw
    bp=i
    min1=arr[0]
    min2=arr[bp]
    final_min=min(min1, min2)
    print(final_min)


#using bianry search
def shiftedMinArr(arr, n):
    #finding the break point of array from where it is shifted
    start=0
    end=n-1
    bp=0
    if n==1:
        return arr[0]
    while start<end:
        mid=(start+end)//2
         
        if arr[mid]>arr[mid+1]:
            bp=mid+1
            return arr[mid+1]
        if arr[mid-1]>arr[mid]:
            bp=mid
            return arr[mid]


        if arr[mid]>arr[0]:
            start=mid+1
        elif arr[mid]<arr[0]:
            end=mid-1
        
    return arr[bp]

            





            



arr=[4,5,6,7,0,1,2]
        
print(shiftedMinArr(arr, len(arr)))


    

