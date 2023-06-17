def superReducedString(s):
    # Write your code here
    res=''
    for i in range(0, len(s)-1):
        if s[i]==s[i+1]:
            i+=1
        else:
            res+=s[i]
    return res 

def removeDuplicate(a, n):
    l = [0]*n
    i=0 
    k=1
    l[0] = a[0]
    for i in range(1, n):
        if a[i-1] != a[i]:
            l[k] = a[i]
            k+=1

    return l

#ins=input()
ins=[1,2,3,3,4,5,6]
print(removeDuplicate(ins, len(ins)))
# s='aaabccddd'
# res=''
# i=0
# while(i<len(s)-1):
#     if s[i]==s[i+1]:
#         i+=1
#     else:
#         res+=s[i]
#     i+=1
# print(res)
