def findDuplicates(arr):
    dict={}
    for i in arr:
        dict[i]=0
    for i in arr:
        dict[i]+=1
    for i in dict.keys():
        if dict[i]>1:
            print(i)


arr=[1,1,3,4,5,1,32,1]
findDuplicates(arr)

