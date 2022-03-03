def longestMountainArray(arr):
    n=len(arr)
    ans=0
    start=0
    end=0
    while start<n:
        end=start
        if end+1 < n and arr[end] < arr[end+1]:
            #here we search for increasing seq and increment end 
            while end+1 <n and arr[end]<arr[end+1]:
                end+=1
            #after this is arr[end]>arr[end+1] means peak is reached
            #so now we start goig down towards valley
            if end+1<n and arr[end] > arr[end+1]:
                while end+1<n and arr[end]>arr[end+1]:
                    end+=1
                ans = max(ans, end-start+1)
        start=max(end, start+1)
    return ans


ls=[2,2,2]
print(longestMountainArray(ls))

# class Solution(object):
#     def longestMountain(self, A):
#         N = len(A)
#         ans = base = 0

#         while base < N:
#             end = base
#             if end + 1 < N and A[end] < A[end + 1]: #if base is a left-boundary
#                 #set end to the peak of this potential mountain
#                 while end+1 < N and A[end] < A[end+1]:
#                     end += 1

#                 if end + 1 < N and A[end] > A[end + 1]: #if end is really a peak..
#                     #set 'end' to right-boundary of mountain
#                     while end+1 < N and A[end] > A[end+1]:
#                         end += 1
#                     #record candidate answer
#                     ans = max(ans, end - base + 1)

#             base = max(end, base + 1)

#         return ans