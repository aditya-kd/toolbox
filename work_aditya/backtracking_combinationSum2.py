def backtrack(candidate, idx, target, partSol, allSol):
    if target==0:
        allSol.append(partSol)
    elif idx==len(candidate):
        return 
    elif target<0:
        return
    else:
        temp_list=partSol[::]
        temp_list.append(candidate[idx])
        target-= candidate[idx]
        backtrack(candidate, idx+1, target, temp_list, allSol)
        target+= candidate[idx]
        k=1
        while idx+k < len(candidate) and candidate[idx] == candidate[idx+k]:
            k+=1
        backtrack(candidate, idx+k, target, partSol, allSol)

def combSum2(candidate, target):
    candidate.sort()
    allSol=[]
    partSol=[]
    backtrack(candidate, 0, target, partSol, allSol)
    return allSol

candidates = [10,1,2,7,6,1,5]
target=8
print(combSum2(candidates, target))

