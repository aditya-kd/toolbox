# def solve(instr1, instr2):
#     mpa={}
#     mpb={}
#     for i in instr1:
#         mpa[i]=mpa.get(i,0)+1
#     for j in instr2:
#         mpb[j]=mpb.get(j, 0)+1
#     key1=mpa.keys()
#     key2=mpb.keys()
#     lena= len(key1)
#     lenb= len(key2)
#     if lena!=lenb:
#         return 'IMPOSSIBLE'
#     else:

# for x in range(int(input())):
#     print("Case #", end="")
#     print(x+1, end="")
#     print(": ", end="")
#     s1 = input()
#     s2 = input()
def solve(s1, s2):
    m = len(s1)   
    n = len(s2)
    i = 0
    j = 0
    cnt = 0
    while(j < n and i < m):
        if(s1[i] == s2[j]):
            i+=1
        else:
            cnt+=1
        j+=1
    if(i == m):
        return (cnt + n-j)
    else:
        return "IMPOSSIBLE"
    
t=int(input())
x=1

while t>0:
    
    a=input()
    b=input()
    print('Case #',end='')
    print(x, end='')
    print(': ',end='')
    print(solve(a, b))
    t-=1
    x+=1
