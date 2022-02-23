def combinationSum(candidates,target):
    all=[]
    par=[]
    bt(candidates, 0, target, par, all)
    return all
def bt(candidate, idx, target, par, all):
    if target==0:
        all.append(par)
        return 
    if idx==len(candidate):
        return
    #without
    bt(candidate,idx+1, target, par, all)

    #with
    # if target- candidate[idx]>=0:
    if target>= candidate[idx]:
        par.append(candidate[idx])
        bt(candidate,idx, target-candidate[idx], par, all)
        par.pop()
