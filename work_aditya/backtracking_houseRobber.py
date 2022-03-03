# def backtrack(nums, n, partSol, allSol):
#     if n==0:
#         allSol= max(allSol, partSol)
#         return
#     elif n==1:
#         allSol = max(allSol, partSol+nums[0])
#         return 
#     #without
#     backtrack(nums, n-1, partSol, allSol)
#     #with
#     # partSol += nums[n-1]
#     temp=partSol
#     temp+=nums[n-1]
#     backtrack(nums, n-2, temp, allSol)

# def solve(nums):
#     nums.sort()

#     partSol=0
#     allSol=0
#     backtrack(nums, len(nums), partSol, allSol)
#     return allSol

# nums = [2,7,9,3,1]
# print(solve(nums))
    

#mark2
#1st working approach
def memfunc(nums,n, tbl):
    if tbl[n]>0:
        return tbl[n]
    if n==0:
        tbl[n]=0
    elif n==1:
        tbl[n]=nums[0]
    else:
        wo=memfunc(nums, n-1, tbl)
        withed=nums[n-1]+memfunc(nums, n-2, tbl)
        print('with, without', withed, wo)
        tbl[n]= max(wo, withed)
    return tbl[n]


def solve(nums):
    mp=[0]*(len(nums)+1)
    optimal=memfunc(nums, len(nums),mp)
    return optimal
#approcach2 memoization with an array
def memofunArr(nums, n, tbl):
    if tbl[n]!=-1:
        return tbl[n]
    if n==0:
        tbl[n]=0
    elif n==1:
        tbl[n]=nums[0]
    else:
        without = memofunArr(nums, n-1, tbl)
        withed= nums[n-1]+memofunArr(nums, n-2, tbl)
        tbl[n] = max(without, withed)
    return tbl[n]
def solve2(nums):
    tbl=[-1]*(len(nums)+1)
    ans=memofunArr(nums, len(nums), tbl)
    return ans
#arpproach 3 dp bottom up
def dpBottomUp(nums):
    n=len(nums)
    if n==0: return 0
    tbl=[0]*(n+1)
    tbl[0]=0
    tbl[1]=nums[0]
    for i in range(2, n+1):
        tbl[i] = max(tbl[i-1], nums[i-1]+tbl[i-2])
    return tbl[n]
#we need only three cells to store results two for previous and 1 for current
def dbBottom3cells(nums):
    n=len(nums)
    if n==0: return 0
    tbl=[0,0,0]
    tbl[0]=0
    tbl[1]=nums[0]
    for i in range(2, n+1):
        tbl[i%3]= max(tbl[(i-1)%3], nums[i-1]+tbl[(i-2)%3])
    return tbl[n%3]
nums = [1,2,3,1]
nums = [2,7,9,3,1]
print(solve(nums))


