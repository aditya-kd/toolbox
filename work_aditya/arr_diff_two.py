def twoDiff(arr, k):
    mp={}
    for i in arr:
        mp[i]=mp.get(i,0)+1
    for x in arr:
        diff = k+x
        if diff in mp.keys():
            print(x, diff)
    
ls=[1,2,3,4]

ls=[1,5,3,4,2]

k=2
twoDiff(ls, k)
