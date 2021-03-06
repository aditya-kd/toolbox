def countInversions1(arr):
    inverts=0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                inverts+=1
    return inverts
    
#APPROACH by tweaking mergesort with a temp array
def countInversion2(arr, n):
	temp_arr = [0]*n
	return _mergeSort(arr, temp_arr, 0, n-1)
def _mergeSort(arr, temp_arr, left, right):
	inv_count = 0
	if left < right:
		mid = (left + right)//2
		inv_count += _mergeSort(arr, temp_arr,left, mid)
		inv_count += _mergeSort(arr, temp_arr,mid + 1, right)
		inv_count += merge(arr, temp_arr, left, mid, right)
	return inv_count
def merge(arr, temp_arr, left, mid, right):
	i = left	 # Starting index of left subarray
	j = mid + 1 # Starting index of right subarray
	k = left	 # Starting index of to be sorted subarray
	inv_count = 0
	while i <= mid and j <= right:

		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:
			temp_arr[k] = arr[j]
			inv_count += (mid-i + 1)
			k += 1
			j += 1

	while i <= mid:
		temp_arr[k] = arr[i]
		k += 1
		i += 1

	while j <= right:
		temp_arr[k] = arr[j]
		k += 1
		j += 1

	for loop_var in range(left, right + 1):
		arr[loop_var] = temp_arr[loop_var]

	return inv_count

arr=[3,2,1]
print(countInversions1(arr))
print(countInversion2(arr, len(arr)))


