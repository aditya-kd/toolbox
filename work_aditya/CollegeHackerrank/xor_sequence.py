from gettext import find


def findXor(n):
    r=n%8
    if r==0 or r==1:
        return n
    elif r==2 or r==3:
        return 2
    elif r==4 or r==5:
        return n+2
    else:#for r==6 and 7
        return 0

# for i in range(10):
#     print(findXor(i+1))
def solve(l, r):
    return findXor(r)^ findXor(l-1)

print(solve(2,8))



