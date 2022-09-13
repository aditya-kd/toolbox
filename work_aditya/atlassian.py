logs=[[0,5],[1,2],[0,5],[1,3]]
# logs=[[0,5],[1,2],[0,2],[0,5],[1000,3]]
logs=[[0,5], [1,2], [0,2], [0,5], [1,3],[3,4],[3,4],[3,5]]
#for storing the user log session 
mp={}
def createFrequency():
    #find the frequency of each user log time
    #O(N)
    for item in logs:
        mp[item[0]]=set()
    
    #setting the user time in each user id key
    #O(N)
    for log in logs:
        user_id= log[0]
        time = log[1]
        mp[user_id].add(time)

    

def getActiveTime(userid):
    
    #O(q)
    if userid not in mp.keys():
        print("Not existing")
        return 0
    #(q)
    return len(mp[userid])


queries=[0,1,4,100,1,0]
#O(q)*2
createFrequency()

# print(mp)
for q in queries:
    print("query", q, "=",getActiveTime(q))


#O(N)*2 + O(q)*O(N)*2





