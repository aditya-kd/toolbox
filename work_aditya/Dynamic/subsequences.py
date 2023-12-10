# Returns all the subsequences that sum to target
def findSum(idx, arr, ds, curSum, targetSum, n):
    if idx == n:
        if curSum == targetSum:
            print(arr)
        return
    
    arr.append(ds[idx])
    curSum += ds[idx]

    findSum(idx+1, arr, ds, curSum, targetSum, n)
    
    arr.pop()
    curSum -= ds[idx]

    findSum(idx+1, arr, ds, curSum, targetSum, n)
    return 

# Returns one/1 subsequence that sums to the target
def findSum(idx, arr, ds, curSum, target, n):
    if idx == n:
        if curSum == target:
            print(arr)
            return True
    
    arr.append(ds[idx])
    curSum += ds[idx]

    if findSum(idx+1, arr, ds, curSum, target, n) == True:
        return True

ds = [1,2,3, 4, 5]
n = len(ds)
ss = 5
arr = []
findSum(0, arr, ds, 0, ss, n)