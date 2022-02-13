# def facto(n):
#     if n==1:
#         return 1
#     return n*facto(n-1)

# def isPrime(n, i):

#     if n<i*i:
#         return True
#     if n%i==0:
#         return False
#     if i==0 or i==1:
#         return False
#     else:
#         return isPrime(n, i+1)
    
# def findNumberInWords(input, place):
#     ones=['','one','two','three','four', 'five', 'six','seven', 'eight', 'nine', 'ten', 
#     'eleven', 'twelve', 'thirteen', 'forteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen','twenty']

#     n=input%10
#     if n==0:
#         return ''
#     if place==1:
#         ans= ones[n]
#     if place==3:
#         ans= ones[n]+'hundred and'
#     if place==4:
#         ans= ones[n]+'thousand and '
#     return findNumberInWords(input//10, place+1)+ans


# print(findNumberInWords(224,1))

    
# # print(isPrime(6,2))
# # print(isPrime(3,2))
# # print(isPrime(17,2))

########################## Friday-10th Dec,21 #########################

def solve(n, k,t, j):
    if n==0 and k==0:
        return t
    if n<0 or k<0:
        return 
    
    for i in range(j,10):
        t.append(i)
        solve(n-j, k-1,t,j+1)

t=[]





