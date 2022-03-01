def waiter(number, q):
    # Write your code here
    prime = [2,3]
    for i in range(5,10001):
        flag=False
        j=2
        while(j*j<=i):
            if(i%j==0):
                flag=True
            j+=1
        if(flag==False):
            prime.append(i)

    answers=[]
    b=[]
    c=[]
    k=0
    currp = prime[0]
    while(k<q):
        while(len(number)!=0):
            x=number.pop()
            if(x%currp==0):
                b.append(x)
            else:
                c.append(x)
        k+=1
        currp = prime[k]
        while(len(b)!=0):
            answers.append(b.pop())
        number=c[:]
        c=[]
        
    while(number):
        answers.append(number.pop())
    return answers