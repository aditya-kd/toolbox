def areFactor(i, arr):
    for x in arr:
        if i%x!=0:
            return False
    return True

def isFactor(arr, i):
    for x in arr:
        if x%i!=0:
            return False
    return True

def getTotalX(a, b):
    # Write your code here
    s=max(a)
    t=min(b)
    total=0
    for i in range(s,t+1):
        if areFactor(i, a)==True and isFactor(a, i)==True:
            total+=1
    return total
        