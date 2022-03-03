def paintHouse( cost):

    # dp=[0]*(house+1)
    for i in range(1, len(cost)):
        cost[i][0]+= min(cost[i-1][1], cost[i-1][2])
        cost[i][1]+= min(cost[i-1][0], cost[i-1][2])
        cost[i][2]+= min(cost[i-1][1], cost[i-1][0])

    return min(cost[-1])

import math
def paintHouse2(cost,n, k):

    for i in range(1, n):
        for j in range(len(cost[0])):
            mnm= math.inf
            for k in range(len(cost[0])):
                if j!=k:
                    mnm = min(cost[i-1][k], mnm)
            cost[i][j]+=mnm
            print(cost)

    return min(cost[-1])

def paintHouseMethod(cost, n, k):
    m1=math.inf
    m2=math.inf
    for i in range(len(arr[0])):
        if cost[0][i] < m1:
            m2=m1
            m1=cost[0][i]
        elif m2< cost[0][i]:
            m2=cost[0][i]
        
    for i in range(1, len(cost)):
        nm1=math.inf
        new_min2=math.inf
        for k in range(len(cost[i])):
            if m1==cost[i-1][k]:
                cost[i][k]+=m2
            else:
                cost[i][k]+=m1
            if cost[i][k]< nm1:
                new_min2=nm1
                nm1=cost[i][k]
            elif cost[i][k]<m2:
                new_min2=cost[i][k]
        m1=nm1
        m2=new_min2

    return min(cost[-1])

        
arr=[[14,2,11],[11,14,5],[14,3,10]]
print(paintHouseMethod(arr, 3, 3))
