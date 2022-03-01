def checkPalindrome(s, k):
    l=0
    r=len(s)-1
    changes=[False]*len(s)
    while(l<r and k>0):
        
        if s[l]>s[r]:
            s[r]=s[l]
            k-=1
            changes[r]=True
        elif s[l]<s[r]:
            s[l]=s[r]
            k-=1
            changes[l]=True
        else:
            l+=1
            r-=1
    print(s)
    print(changes)
    print(k)
    if k==0:
        print(s)
    
    l=0
    r=len(s)-1
    while (l<r and k>0):

        if s[l]!=9:
            if changes[l]==True or changes[r]==True:
                #restore
                k+=1
                k-=2
                s[l]=9
                s[r]=9
                l+=1
                r-=1
            else:
                s[l]=9
                s[r]=9
                k-=2
    print('Final Value of K')
    print(k)
    if k<0:
        print(-1)
    else:
        
        print(s)

checkPalindrome(list('092282'), 3)

