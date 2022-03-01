def largestPermutation(arr,k):
    n=len(arr)
    #contrlled selection sort
    for i in range(0, n-1):

        if k>0:
            maxm = i
            for j in range(i+1, n):
                if arr[j]> arr[maxm]:
                    maxm= j
            if maxm != i:
                temp =arr[maxm]
                arr[maxm]= arr[i]
                arr[i] =temp
                k-=1
        else: break

#greedy solution- does not give a TLE on Hackerrank
def largestPermut2(arr, k):
    n=len(arr)
    mp={}#index value pair
    for i in range(n):
        mp[arr[i]]=i
    for i in range(n):
        if k==0: break
        if arr[i]==n-i: continue
        #swapping position in map
        temp= mp[n-i]
        mp[arr[i]] = mp[n-i]
        mp[n-i] = i
        #swapping positin in arr
        arr[temp], arr[i] = arr[i], arr[temp]
        k-=1
arr=[4,5,2,1,3]
n=len(arr)
k=3
largestPermut2(arr, k)
print(arr)

        