def maxSlidingWindwo(arr, k):

    for i, item in enumerate(arr):
        print(i, item)

    # i = 0
    # j = 0
    # maxNum = arr[i]
    # ans = []
    # n = len(arr)

    # while j < n:
    #     maxNum = max(maxNum, arr[j])

    #     if j - i + 1 < k:
    #         j += 1
        
    #     elif j - i + 1 == k:
    #         maxNum = max( maxNum, arr[j])
    #         ans.append(maxNum)
    #         i += 1
    #         # maxNum = arr[i]
    #         j += 1

    # return ans

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print( maxSlidingWindwo(nums, k))