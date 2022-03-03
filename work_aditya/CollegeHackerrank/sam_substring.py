def substring2(str, n):
    total=0
    for i in range(len(str)):
        temp=''
        for j in range(i,n):
            temp+=(str[j])
            print(temp)
            total+=int(temp)
    return total


s='1234'
n=len(s)
print(substring2(s,n))