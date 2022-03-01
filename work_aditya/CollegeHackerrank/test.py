

def commonChild(s1, s2):
    # Write your code here
    arr=[]
    for i in range(0,len(s1)):
        ls=[0]*len(s1)
        arr.append(ls)        
    
    m=len(s1)
    for i in range(0, m):
        for j in range(0, m):
            if s1[i-1]==s2[j-1]:
                arr[i][j]=arr[i-1][j-1]+1
            else:
                arr[i][j]=max(arr[i][j-1], arr[i-1][j])
                       
    return arr[m-1][m-1]

s1='SHINCHAN'
s2='NOHARAAA'
print(commonChild(s1, s2))
