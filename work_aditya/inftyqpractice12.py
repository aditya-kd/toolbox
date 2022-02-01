def function(n, earn, cost):
    extra=0
    remaining=0

    for i in range(len(earn)):
        
        if cost[i] > (earn[i]+extra):
            remaining+= cost[i]-earn[i]-extra
            
        elif cost[i] <= (earn[i]):
            extra += earn[i]- cost[i]
        
        elif cost[i] <= (earn[i]+extra):
            extra = earn[i]+extra - cost[i]

    print(extra)    
    print('answer',remaining)


n=3
earn=[3,4,2]
cost=[5,3,4]
# earn=[3,4,2,7,8,5,3]
# cost=[5,3,4,6,7,7,5]
function(n, earn, cost)