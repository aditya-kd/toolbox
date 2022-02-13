#using two loops
def findFirstNonRepeatin(arr):
    n=len(arr)
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i]==arr[j]:
                print('First Non Repeating character: ', arr[i])

#using hashing
def firstNonRepeating(arr):
    mp={}
    for i in arr:
        mp[i]=0
    #store frequency
    for i in range(0, len(arr)):
        mp[arr[i]]+=1
    for i in arr:
        if mp[i]>1:
            print('First Non Repaeting is: ', i)
            break
arr=[7,8,5,6,2,6,1]
findFirstNonRepeatin(arr)
firstNonRepeating(arr)

    
