def isUnique(arr):
        ls=[False]*26
        for i in range(len(arr)):
            index=ord(arr[i])-ord('a')
            if ls[index]==True:
                return False
            else:ls[index]=True
        return True
       
def countGoodSubstrings(arr):
    s=0
    e=2
    total=0
    while e<len(arr):
        if isUnique(arr[s:e+1])==True:
            total+=1
        s+=1
        e+=1
    return total

s = "xyzzaz"
print(countGoodSubstrings(s))