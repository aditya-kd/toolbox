def partition(arr, l, r):
  pivot= arr[r]
  i= l-1
  for j in range(l, r):
    if arr[j] <= pivot:
      i+=1
      arr[i],arr[j]=arr[j],arr[i]
  arr[i+1],arr[r] = arr[r],arr[i+1]
  return i+1

def quickselect(arr, left, right, k):

    index= partition(arr, left, right)
    if (index-left ==k-1):
        return arr[index]
    if( index - left> k-1):
        return quickselect(arr, left, index-1, k)
    return quickselect(arr, index+1, right, k-index+left-1)


arr=[78,-90,11,12,23,34,45]
print(quickselect(arr, 0, len(arr)-1, 2))
print(quickselect(arr, 0, len(arr)-1, 1))
print(quickselect(arr, 0, len(arr)-1, 3))
print(quickselect(arr, 0, len(arr)-1, 5))
print(quickselect(arr, 0, len(arr)-1, 2))

