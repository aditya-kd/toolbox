# def sumOdd(n):
#     terms = (n + 1)//2
#     sum1 = terms * terms
#     return sum1
def suminRange(l, r):
    roddSum= (r+1)//2
    roddSum=roddSum*roddSum
    loddSum=(l)//2
    loddSum=loddSum*loddSum
    return roddSum-loddSum
def sumEven(l, r):
    r=int(r/2)
    rsum=int(r*(r+1))
    l=int((l-1)/2)
    lsum=int(l*(l+1))
    return rsum-lsum
 
def solve(l,r):
    evenSum=sumEven(l, r)
    oddSum= suminRange(l,r)
    print(evenSum, oddSum)
    return evenSum-oddSum

print(solve(10,14))