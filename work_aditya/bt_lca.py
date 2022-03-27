def solve(ss):
    ls= list(ss)
    count=0
    for i in range(0, len(ss)-2):
        if ls[i]==ls[i+1] and ls[i+1]!=ls[i+2]:
            ls[i+2]= ls[i]
            count+=1
    return count

ss='abc'
ss='aabcc'
print(solve(ss))
