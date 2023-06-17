def rotate_array(arr, start_index, end_index, num_rotations):
    """
    Rotate the elements of an array from start_index to end_index by num_rotations
    """
    # Calculate the number of elements to be rotated
    n = end_index - start_index + 1

    # Perform the rotations
    for i in range(num_rotations):
        temp = arr[start_index]
        for j in range(start_index, start_index + n - 1):
            arr[j] = arr[j + 1]
        arr[start_index + n - 1] = temp

    # Return the rotated array
    return arr

def find_mid_index(n):
    """
    Find the mid index of an array of size n
    """
    if n % 2 == 0:
        # If n is even
        return n // 2 - 1, n // 2
    else:
        # If n is odd
        return n // 2




n= int(input())
arr = list(map(int, input().split()))
p = int(input())
cpy = arr[::]
midindex = n//2
old = arr.index(p)
arr = arr[midindex:] + arr[:midindex]
newindex = arr.index(p)
ans = newindex + old * cpy[newindex]
print(arr)
print(ans)


# midindex = n//2
# old = arr.index(p)
# arr1 = rotate_array(arr, 0, midindex, 1)
# print(arr1)
# arr2 = rotate_array(arr1, midindex, n-1, 1)
# print(arr2)
# arr3 = arr2[::-1]
# print(arr3)
# newind = arr3.index(p)


# ans = newind+old*cpy[newind]
# print(ans)


