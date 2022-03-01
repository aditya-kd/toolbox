import math
def encrypt(s):
    ss=''
    for i in range(0,len(s)):
        if s[i]==' ':
            continue
        else:
            ss=ss+s[i]

    # print('Space removed ',ss)
    # print('Length: ',len(ss))
    L=math.sqrt(len(ss))
    rows=math.floor(L)
    col=math.ceil(L)
    # print('Square Root: ', L)
    # print('Rows-Columns: ', rows, col)
    s=ss
    for i in range(0,8):
        sp=0
        new_s=''
        while((i+sp)<len(s)):
            print(s[i+sp],end='')
            #new_s=new_s+s[i+sp]
            sp+=8
        print(end=' ')


s='if man was meant to stay on the ground god would have given us roots'
encrypt(s)
