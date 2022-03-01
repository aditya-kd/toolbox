

def mergeSort(m):
    if len(m) <= 1:
        return [0, m]
    mid = len(m)//2
    l = []
    r = []
    for i in range(mid):
        l.append(m[i])
    for i in range(mid, len(m)):
        r.append(m[i])
    left = mergeSort(l)
    right = mergeSort(r)
    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    result = []
    num = left[0] + right[0]
    while i < len(left[1]) or j < len(right[1]):
        if i < len(left[1]) and j < len(right[1]):
            if left[1][i] <= right[1][j]:
                result.append(left[1][i])
                i += 1
                num += j
            else:
                result.append(right[1][j])
                j += 1
        elif i < len(left[1]):
            result.append(left[1][i])
            i += 1
            num += j
        elif j < len(right[1]):
            result.append(right[1][j])
            j += 1
    return [num, result]

T = int(input())
for i in range(T):
    n = int(input())
    nums = [int(i) for i in input().split()]
    print(mergeSort(nums)[0])