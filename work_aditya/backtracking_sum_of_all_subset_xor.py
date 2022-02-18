def backtrack(nums, n, currXorTotal, sumofAllXor):
    if n==0:
        sumofallxortotal+= currXorTotal
        return
    idx = n-1
    backtrack(nums, n-1, currXorTotal, sumofallxortotal)
    currentxortotal = currentxortotal
def subsetXor(nums):
    sumofAllXorTotla=0
    currentXorTotal= 0
    backtrack(nums, len(nums), currentXorTotal, sumofAllXorTotla)
    return sumofAllXorTotla

