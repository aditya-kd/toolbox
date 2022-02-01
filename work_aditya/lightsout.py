matrix=[[1, 0, 0], [0, 0, 0], [0, 0, 1]]
# for i in range(3):
#     ls= list(map(int, input().split()))
#     matrix.append(ls)
# print(matrix)
ans=[[1,1,1],[1,1,1],[1,1,1]]

for i in range(3):
    for j in range(3):
        res=0
        if matrix[i][j]%2 == 0:
            res=1
        else:
            res=0

        if i-1 >=0:
            ans[i-1][j]= res
        if j-1 >=0:
            ans[i][j-1]=res
        if j+1<= 2:
            ans[i][j+1]=res
        if i+1<=2:
            ans[i+1][j]=res
print(ans)

matrix=[]
for i in range(3):
    row=list(map(int, input().split()))
    matrix.append(row)
initial=[[1 for col in range(3)] for row in range(3)]

for i in range(3):
    for j in range(3):
        count= matrix[i][j]
        if count%2==1:
            initial[i][j]= int(not initial[i][j])
            if i>0:
                initial[i-1][j]=int(not initial[i-1][j])
            if i<2:
                initial[i+1][j]=int (not initial[i+1][j])
            if j>0:
                initial[i][j-1]= int(not initial[i][j-1])
            if j<2:
                initial[i][j+1]= int(not initial[i][j+1])

for i in range(3):
    for j in range(3):
        print(initial[i][j], end='')
    print()

