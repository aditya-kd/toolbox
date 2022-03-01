def solve(container):
    rows=len(container)
    cols=len(container[0])
    cont=[0]*rows
    type=[0]*cols
    
    for i in range(rows):
        cont[i]= sum(container[i])
    for j in range(cols):
        ss=0
        for i in range(rows):
            ss+= container[i][j]
        type[j]=ss
    
    if sorted(type)==sorted(cont):
        return 'Possible'
    else:
        return 'Impossible'


arr=[[1,4],[2,3]]
print(solve(arr))
            