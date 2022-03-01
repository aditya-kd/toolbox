def substring2(str, n):
    stuart=0
    kevin=0
    kl=set()
    sl=set()
    for i in range(len(str)):
        temp=''
        for j in range(i,n):
            temp+=str[j]
            if temp[0] in 'aeiou':
                kl.add(temp)
            else:
                sl.add(temp)
    for item in kl:
        kevin+=str.count(item)
    for item in sl:
        stuart+=str.count(item)
    if kevin>stuart:
        return 'Kevin'+kevin
    else:
        return 'Stuart'+stuart

def minion_game(string):
    sc=0
    kv=0
    n=len(string)
    v=['A','E','I','O','U']
    for i in range(len(string)):
        if string[i] in v:
            kv+=n-i
        else:
            sc+=n-i
    if sc>kv:
        print('Stuart',sc)
    elif kv>sc:
        print('Kevin',kv)
    else:
        print('Draw')

substring2('banana',len('banana'))