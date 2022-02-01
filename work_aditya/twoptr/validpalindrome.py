def isPalindrome( ss):
        if len(ss)==1:
            return True
        s=''
        for i in ss:
            if i!=' ':
                s+=i
        print(s)
        i=0
        e=len(s)-1
                
        while(i<e):
            if s[i]!=s[e]:
                return False
            i+=1
            e-=1
        return True

print(isPalindrome('race a car'))
