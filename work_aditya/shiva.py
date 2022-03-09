def substring2(str):
    n=len(str)
    score=0
    for i in range(len(str)):
        temp=''
        for j in range(i,n):
            temp+=str[j]
            print(temp)
            if int(temp)%3==0:
                score+=1
    return score

ss=input()
print(substring2(ss))
