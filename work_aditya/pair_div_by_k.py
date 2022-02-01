def arrange(arr, k):
        d={}
        n=len(arr)
        r= [0]*k
        
        for i in range(n):
            r[arr[i]%k] += 1
        
        pairs=0
        for i in range(k//2+1):
            if i==0:
                if r[i]%2 !=0:
                    return False
                else:
                    pairs += r[i]//2
            elif i==k-1:
                if r[i]%2 !=0:
                    return False
                else:
                    pairs += r[i]//2
            else:
                if r[i] != r[k-i]:
                    return False
                else:
                    pairs += r[i]//2
                    
        return True