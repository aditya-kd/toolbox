def frogjump(stones):
    n=len(stones)
    destination=stones[n-1]
    mp={}
    for i in stones:
        mp[i]=set()
    print(mp)
    mp[stones[0]].add(1)
    for i in range(len(stones)):
        curr_stones_pos =stones[i]
        for jump in mp[curr_stones_pos]:
            next_pos=curr_stones_pos+jump
            if curr_stones_pos+jump==destination:
                return True
            if curr_stones_pos+jump in mp:
                mp[next_pos].add(jump)
                mp[next_pos].add(jump-1)
                mp[next_pos].add(jump+1)
    return False
            


        
        


ls=[0,1,3,4,6,8,12,17]
frogjump(ls)