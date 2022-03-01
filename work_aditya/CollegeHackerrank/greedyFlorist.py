def greedyFlirist(k,c):
    i=0
    total=0
    c.sort(reverse=True)
    for i in range(len(c)):
        
        total+= ((i//k)+1)*c[i]
        
    return total

#this is only one approach
def findCol(r, c):
    s=0
    if r%2==0:
        s=5*(r-2)+1
        print(s)
    else:
        s=5*(r-1)
        print(s)
    c=2*(c-1)
    print(c)
    # print('Findal',s+c)

findCol(5,1)
findCol(5,2)
findCol(5,3)
findCol(5,4)
def greedyFlirist(k,c):
    i=0
    total=0
    c.sort(reverse=True)
    for i in range(len(c)):
        
        total+= ((i//k)+1)*c[i]
        
    return total

#this is only one approach
def findCol(r, c):
    s=0
    if r%2==0:
        s=5*(r-2)+1
        #print(s)
    else:
        s=5*(r-1)
        #print(s)
    c=2*(c-1)
    #print(c)
    #print('Findal',s+c)
    return s+c

findCol(4,2)
findCol(4,3)
findCol(4,4)
findCol(4,1)
findCol(4,5)
findCol(6,3)
