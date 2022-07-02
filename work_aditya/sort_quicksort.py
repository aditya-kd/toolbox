def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:

      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quicksort(arr,low, high):
  if low<high:
    p = partition(arr, low, high)
    print('Pivot',p,'Pass',arr)
    quicksort(arr, low, p-1)
    print('Pivot',p,'Pass',arr)
    quicksort(arr, p+1, high)
    print('Pivot',p,'Pass',arr)


arr=[78,-90,45,23,34,11,12]
n= len(arr)
quicksort(arr, 0, n-1)
print('Quicksort output',arr)
arr.reverse()

print('New QuickSort')
quicksort(arr,0,n-1)
print(arr)