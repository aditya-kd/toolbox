#find the cele leet code 277
def findJudge(n, trust):
    youTrust=[0]*(n+1)
    trustYou=[0]*(n+1)
    for entry in trust:
        youTrust[entry[0]]+=1 #outdegree
        trustYou[entry[1]]+=1 #indegree

    for i in range(1,n+1):
        if youTrust[i]==0 and trustYou[i]==(n-1):
            return i

    return -1