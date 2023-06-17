arr=list(map(int,input().split()))
arr.sort()
target=int(input())
def twosum(arr,target):
    i,j=0,len(arr)-1
    while i<j:
        if arr[i]+arr[j]==target:
            return True
        if arr[i]+arr[j]<target:
            i+=1
        else:
            j-=1
    return False

print(twosum(arr,target))














