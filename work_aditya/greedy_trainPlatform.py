def findPlatforms(timing, trains, platform ):
    data=[]
    for i in range(platform+1):
        data.append([])
    # print(data)
    # data=[[],[],[]] 
    for train in timing:
        pt=train[2]
        dept=train[1]
        arr=train[0]
        temp=data[pt]
        # print('Pt',pt, 'temp', temp)
        # print('temp:',temp)
        temp.append([dept,arr])
        data[pt]=temp
        temp=[]
    print(data)


        #input according to platform taken here

        #now sorting according to dept time
    for i in range(1, len(data)):
        # print(data[i][0][1])
        data[i].sort()
    # print(data)
        #sorting completeccvccv  bn nn jn jjnjjmmjjmjmmkmkkkmkmk   b b b    n fcvuv   b bgg bg  b bbbnn nbz
    
    total=0
    for curPt in data:
        if len(curPt)==0:
            continue
        x=0
        total+=1
        for curTrainIndex in  range(len(curPt)):
            if curPt[curTrainIndex][1] >= curPt[x][0]:
                x=curTrainIndex
                total+=1

        print('Next Platform')
        
    print("Count", total)

arr=[]
t1=[1000,1030,1]
t2=[1010,1020,1]
t3=[1025,1040,1]
t4=[1130,1145,2]
t5=[1130,1140,2]
arr=[t1,t2,t3,t4,t5]
# print(arr)
train=5
platform =2
findPlatforms(arr, train, platform)
