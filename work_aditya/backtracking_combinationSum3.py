def combinationSum3(k, n):
    #creating array for 1 to n
    candidate=[i for i in range(1, 10)]
    # print(candidate)
    allSol=[]
    partSol=[]
    backtrack(candidate, 0, k,n, partSol, allSol)
    return allSol

def backtrack(candidate, idx, k, target, partSol, allSol):
    if target<0:
        return 
    if k==0:
        if target==0:
            allSol.append(partSol)
        return

    if target==0:
        return
    if idx== len(candidate):
        return
    backtrack(candidate, idx+1, k, target, partSol, allSol )
    if target>= candidate[idx]:
        temp_list=partSol[::]
        temp_list.append(candidate[idx])
        backtrack(candidate, idx+1, k-1,target-candidate[idx], temp_list, allSol)

k=3
n=9
print(combinationSum3(k, n))