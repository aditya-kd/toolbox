def binarySearch(arr, n, k):
    start = 0
    end = n-1
    while(start<=end):

        m = (start+end)//2
    #   m = start + (end - start)//2

        if arr[m]==k:
            print('Found at ', m, 'index')
            return m

        elif arr[m]>k:
            end=m-1
        else:
            start=m+1

    print(k,'not found')
    return -1

arr=[-1,0,3,5,9,12]
k=-1
binarySearch(arr, len(arr), k)


        