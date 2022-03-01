permutes=[]
def solve(string, left, right):
    if left == right:
        # print(''.join(string))
        permutes.append(''.join(string))
    for i in range(left, right):
        string[left],string[i]=string[i],string[left]
        solve(string, left+1, right)
        string[left], string[i]=string[i],string[left]

        
def gameOfThrones(s):
    mp={}
    for ch in s:
        mp[ch]=mp.get(ch, 0)+1
    hasOdd=False
    for freq in mp.values():
        if freq%2==1:
            if hasOdd:
                return False
            else:
                hasOdd=True
    return True
s='aaabbbb'
gameOfThrones(s)
