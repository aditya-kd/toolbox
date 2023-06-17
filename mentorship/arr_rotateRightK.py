def rotateArray(arr, n, k):
    backup = arr[:]
    for i in range(0, n):
        idx = (i+k)%n
        arr[idx] = backup[i]

    return arr


def reverse(arr, s, e):
    start = s
    end = e
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateArray2(arr, n, k):

    #reverse complete array
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)

    return arr


input_arr = [1,2,3,4,5]
k = 3
n = len(input_arr)

# print(rotateArray(input_arr, n, k))

print(rotateArray2(input_arr, n, k))



