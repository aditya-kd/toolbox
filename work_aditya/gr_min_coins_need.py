def findNumCoins(notes, amt):
    n=len(notes)
    ans=[]
    i= n-1
    while i>=0:
        while amt>= notes[i]:
            amt-= notes[i]
            ans.append(notes[i])

        i-=1

    print(ans)
    return ans

ls=[1,2,5,10,20,50,100,500,1000]
amt=93
findNumCoins(ls, amt)

