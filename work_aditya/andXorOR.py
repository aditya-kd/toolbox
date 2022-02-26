import sys

def andXorOr(a):
    # Write your code here
    s=[]
    ans=-sys.maxsize
    for i in range(0, len(a)):
        while len(s)>0 and s[-1]>=a[i]:
            x=s.pop()
            ans= max(ans, a[i]^x)
        if len(s)!=0:
            ans= max(ans, a[i]^s[-1])
        
    return ans