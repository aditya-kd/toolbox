def traverse(matrix):
    r=len(matrix)
    c=len(matrix[0])
    for gap in range(0, len(matrix)):
        i=0
        j=gap
        while j<c:
            print(matrix[i][j],',',end='')
            i+=1
            j+=1
        print()
def traverse2(matrix):#adds true and fasle values in digaonals
    r=len(matrix)
    c=len(matrix[0])
    for gap in range(0, len(matrix)):
        i=0
        j=gap
        while j< c:
            matrix[i][j]=True
            i+=1
            j+=1
        print()
# def traverse(matrix):
#     r=len(matrix)
#     c=len(matrix[0]);
#     for gap in range(0, len(matrix)):
#         i=0
#         j=gap
#         while j<c:
#             # print(matrix[i][j],',',end='')
#             if i==j:
#                 matrix[i][j]=True
#             if i!=j and gap==1:
#                 matrix[i][j]=False
#             if i!=j and gap!=1:
#                 if matrix[i]==matrix[j] and matrix[i-1][j-1]:
#                     matrix[i][j]=True

#             i+=1
#             j+=1
#         print()


def akashsir(s):
    n=len(s)
    dp=[[False]*n for i in range(n)]
    for gap in range(n):
        i=0
        j=gap
        while j<n:
            if gap==0:
                dp[i][j] =True
            elif gap==1:
                if s[i] == s[j]:
                    s[i][j]=True
            else:
                if s[i] == s[j] and dp[i+1][j+1]:
                    dp[i][j] = True
            if dp[i][j]:
                ans=s[i:j+1]
            i+=1
            j+=1

    return ans



ls=[]
c=1
for i in range(5):
    temp=[]
    for j in range(5):
        temp.append(c)
        c+=1
    ls.append(temp)
# print(ls)
traverse(ls)
for item in ls:
    print(item)
