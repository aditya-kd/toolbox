def minSwaps(arr):
    clone=arr[:]
    s= sorted(arr)
    mp={}
    for i in range(0, len(arr)):
        mp[arr[i]]=i

    swaps=0
    for i in range(0, len(arr)-1):
        gi= mp[clone[i]]
        bi= mp[s[i]]
        if gi!=bi:
            clone[gi],clone[bi]=clone[bi],clone[gi]
            mp[clone[gi]]=bi
            swaps+=1
    print(swaps)
    print(clone)#this gets printed as sorted
    return swaps

arr=[4,3,1,2,5,6]
minSwaps(arr)
