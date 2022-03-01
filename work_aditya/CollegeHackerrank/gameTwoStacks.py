tb=0
    total=c=0
    hst=[]
    a=a[::-1]
    b=b[::-1]
    while len(a)>0 and total+a[-1]<= maxSum:
        t=a.pop()
        total+=t
        hst.append(t)
        c += 1
        print(c)
    while len(b)>0 and tb + b[-1] <=maxSum:
        if total + b[-1] <= maxSum:
            t=b.pop()
            total+=t
            tb+=t
            c+=1
            print (c)
        else:
            t=b.pop()
            total=total - hst.pop() + t
            tb+=t
    return (c)