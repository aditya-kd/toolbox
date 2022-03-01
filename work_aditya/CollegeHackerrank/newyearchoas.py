def chaos(a, n):
    cnt=0
    for i in range(n-1, -1, -1):
        if a[i]!=(i+1):
            if (a[i-1]==(i+1) and (i-1)>=0):
                cnt+=1
                # swap(a[i], a[i-1])
                a[i],a[i-1]=a[i-1],a[i]

            elif a[i-2]==(i+1) and (i-2)>=0):
                cnt+=2
                # swap(a[i-2],a[i-1])
                a[i-2],a[i-1]=a[i-1],a[i-2]
                a[i-1],a[i]=a[i],a[i-1]
                # swap(a[i-1],a[i])
            else:
                print('too chaotic')
                return
    return cnt