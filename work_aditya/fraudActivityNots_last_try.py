
def getMedian(d, fr):
    s=0
    for i in range(201):
        s+=fr[i]
        if 2*s >d:
            return 2*i
        elif 2*i ==d:
            j=i+1
            while True:
                if fr[j]!=0:
                    return i+j
    return -1
                
def activityNotifications(A,d):
    fr=[0]*(201)
    
    ans=0
    n=len(A)
    for i in range(0, n):
        if i>=d:
            if A[i]>= getMedian(d, fr):
                ans+=1
            fr[A[i-d]]-=1

        fr[A[i]]+=1
    return ans