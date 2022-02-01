def substring1(s,n):
    for i in range(n):
        for len in range(i+1, n+1):
            print(s[i:len])


def substring2(str, n):
    
    for i in range(len(str)):
        temp=''
        for j in range(i,n):
            temp+=str[j]
            print(temp)



def countSubstrings(str, n):
    #any stirng has n*n(n-1)/2 substr that are not empty
    #if we include empyt string then total becomes
    #n*n(n-1)/2 + 1
    return (n*(n+1))//2 +1
str='moomso'
substring2(str,len(str))
print(countSubstrings(str,len(str)))