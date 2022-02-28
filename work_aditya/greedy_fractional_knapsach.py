def fractionalKnapsack(data, capacity):
    data.sort(reverse=True, key=lambda x:x[1]//x[0])#sorting on the basis of ratio
    total=0
    for item in data:
        curwt= item[0]
        curval= item[1]
        print(curwt, curval)
        if capacity-curwt >=0: #subtracting whole values
            capacity-= curwt
            total +=curval
        else:
            fraction = capacity/curwt#substracting fractions
            total+= curval*fraction
            capacity = int(capacity -(curwt*fraction))
            break
    return total

arr=[[10,60],[40,40],[20,100],[30,120]]
capacity= 50
ans=fractionalKnapsack(arr, capacity)
print(ans)


