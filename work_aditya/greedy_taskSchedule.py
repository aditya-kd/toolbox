
def sorter(ele):
    return ele[1]
def taskSchedule(input):
    tasks= sorted(input, key= sorter)
    print(tasks)
    total=0
    i=1
    prev= tasks[0]
    while i<len(tasks):
        curr= tasks[i]
        if prev[1] <=curr[0]:
            total+=1
            prev=curr

        i+=1

    print('Number of Tasks', total)
    return total

ls=[[0,1], [2,6],[4,6],[7,8],[8,9],[3,4]]
taskSchedule(ls)