def findCount2(arr,n, k):
    total=[0]*100
    total[0]=1
    cs=0
    for i in arr:
        cs+=i
        cs%=k
        total[cs]+=1
    count=0
    for i in range(0,k):
        count+= (total[i]*(total[i]-1))//2
    return count
