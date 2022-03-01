def maximumPalinUsingKChanges(strr, k):
    palin = strr[::]
 
    
    l = 0
    r = len(strr) - 1
 
    while (l <= r):
 
        
        if (strr[l] != strr[r]):
            palin[l] = palin[r] =max(strr[l], strr[r])
 
            k -= 1
        l += 1
        r -= 1
 
    
    if (k < 0):
        return "-1"
 
    l = 0
    r = len(strr) - 1
 
    while (l <= r):
 
        if (l == r):
            if (k > 0):
                palin[l] = '9'
 
       
        if (palin[l] < '9'):
 
           
            if (k >= 2 and palin[l] == strr[l] and
                           palin[r] == strr[r]):
                k -= 2
                palin[l] = palin[r] = '9'
 
            
            elif (k >= 1 and (palin[l] != strr[l] or
                              palin[r] != strr[r])):
                k -= 1
                palin[l] = palin[r] = '9'
 
        l += 1
        r -= 1
 
    return palin