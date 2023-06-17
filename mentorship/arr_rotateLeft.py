def reverse(arr, s, e):
    start = s
    end = e
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end  -= 1

def leftRotate(arr, n, k):

    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)

    return arr

def leftRotate2(arr, n, k):
    mod = k%n
    res = [0]*n
    for i in range(0, n):
        idx = (mod+i)%n
        res[i] = arr[idx]
    return res

input_arr = [1,2,3,4,5]
k = 5
n = len(input_arr)

# print(leftRotate(input_arr, n, k))
print(leftRotate2(input_arr, n, k))
