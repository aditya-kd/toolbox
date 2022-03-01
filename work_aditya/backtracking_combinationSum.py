#All unique combinations that sum up to target
def bt(candidate, idx, target, par, all):
    if target==0:
        all.append(par)
        print('all', all)
        return 
    if idx==len(candidate):
        return
    bt(candidate,idx+1, target, par, all)
    # print('partsol',par)
    if target>= candidate[idx]:
        temp_list=par[::]
        temp_list.append(candidate[idx])
        #only one change than template, idx+1 not done, only idx passed
        bt(candidate, idx, target-candidate[idx], temp_list, all)

def combinationSum(candidates,target):
    all=[]
    par=[]
    bt(candidates, 0, target, par, all)
    return all

nums=[2,3,6,7]
k=7
print(combinationSum(nums, k))