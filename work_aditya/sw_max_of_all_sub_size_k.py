from collections import deque
def maxofAllSubK(arr, k):
    ans=[]
    l=deque()
    i=0
    j=0
    if k> len(arr):
        ans.append(max(l))
        return ans
    
    while j<len(arr):
        
        while len(l)>0 and l[-1] <arr[j]:
            l.pop()
        if j-i+1 <k:
            j+=1
        elif j-i+1 ==k:
            ans.append(l[0])
            if l[0]==arr[i]:
                l.popleft()
            i+=1
            j+=1

    return ans


    





    