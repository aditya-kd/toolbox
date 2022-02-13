def getPeak(arr, n):
    max=-float('inf')
    peak=0
    for i in range(n): 
        if max<arr[i]:
            peak=i
            max=arr[i]
    print('Peak element: ', peak)



arr=[24,69,100,99,79,78,67,36,26,19]
arr = [3,4,5,1]
arr = [0,10,5,2]
arr = [0,1,0]
n=len(arr)
getPeak(arr, n)

    
