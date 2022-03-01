import math
def isPower2(x):
    return (x and (not(x & (x - 1))) )
# def lowerPower2(n):
 
#     res = 0;
#     for i in range(n, 0, -1):
         
#         # If i is a power of 2
#         if ((i & (i - 1)) == 0):
         
#             res = i
#             break
         
#     return res

def counterGame(n):
    # Write your code here
    r="Richard"
    s='Louise'
    chance=False
    while n!=1:
            if isPower2(n):
                n=n//2
            else:
                n=n-lowerPower2(n)
            chance= not chance
    #print(chance)
    if chance==True:
        return r
    else:
        return s
        
# print(counterGame(132))
def lowerPower2(n):
    power=math.floor((math.log2(n)))
    return 2**power


#Rahul sir
def pqr(n):
    m=1
    while m<n:
        m*=2
    return m//2

def xyz(n):# both approaches are correct
    if n==1:
        return True
    elif n%2!=0 or n==0:
        return False
    return xyz(n//2)
    # if (n&(n-1))==0:
    #     return True
    # else:
    #     return False
def counterGame(n):
    # Write your code here
    r="Richard"
    s='Louise'
    chance=False
    while n!=1:
            if xyz(n):
                n=n//2
            else:
                n=n-pqr(n)
            chance= not chance
    #print(chance)
    if chance==False:
        return r
    else:
        return s

print(lowerPower2(132))