def insertionsort(arr, n):
    for i in range(1, n):
        temp= arr[i]
        j= i-1

        while j>=0 and temp<arr[j]:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1]= temp
    print(arr)


arr=[78,45, -90, 23, 34, 12, 11]
n=len(arr)
insertionsort(arr, n)

