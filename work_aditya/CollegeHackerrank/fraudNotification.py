def acitivityNotification(expenditure, d):
    mp={}

    def get_med(idx):
        s=0
        for i in range(201):
            freq=0
            if i in mp:
                freq=d[i]
            s+=freq
            if s>=idx:
                return i
    result=0
    for i in range(len(expenditure)):
        val = expenditure[i]
        if i >= d:
            med = get_med(d//2 +d%2)
            if d%2 ==0:
                if val >=med + get_med(d//2 +1 ):
                    result+=1
            else:
                if val>= med*2:
                    result+=1
        if val not in d:
            d[val]=1
        else:
            d[val]+=1
        if i>= d:
            prev= expenditure[i-d]
            d[prev] -=1

    return result
