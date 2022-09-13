
def equalSumSubsetPartition(s):
    sum_neg=0
    sum_pos=0

    for val in s:
        if val<0:
            sum_neg += val
        else: 
            sum_pos += val

    ssum = sum_pos + sum_neg

    if sum & 1:
        return []

    n = len(s)
    dp = {}
    dp[0][s[0]] = True
    for i in range(1, n):
        for val in range(sum_neg, sum_pos+1):
            dp[i][val] = dp[i-1][val]
            if val==s[i] :
                dp[i][val] = True

            elif (val -s[i])>= sum_neg:
                dp[i][val] |= dp[i-1][val -s[i]]

            

    required = ssum//2
    idx = n-1
    #not possible
    if not dp[idx][required]:
        return []

    resultSubset=[0]*n
    cnt =0
    while idx>=0:
        if idx != 0:
            if dp[idx][required] and not dp[idx-1][required]:
                resultSubset[idx] = 1
                cnt +=1
                required -= s[idx]
                if required == 0:
                    break


        else:
            resultSubset[idx] = 1

            cnt+=1


        idx-=1

    if cnt == n:
        resultSubset=[]

    return resultSubset