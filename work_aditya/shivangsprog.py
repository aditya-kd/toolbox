def matches(a, b):
        if a=='1' and b=='0': return True
        else:
            return False

def isValidParenthesis(s):
    stack=[]
    for i in s:
        if i in ['1']:
            stack.append(i)
        else:
            if len(stack)==0:
                return False
            
            elif matches(stack[len(stack)-1], i) == False:
                return False

            stack.pop()

    if len(stack)==0:
        return True
    else: return False

def toBinary(instr):
    bb= str(bin(instr))
    return isValidParenthesis(bb[2:])

def solve(A, l, r):
    total=0
    for i in range(l, r+1):
        if toBinary(A[i])==True:
            print(A[i], 'is valid')
            total+=A[i]
            total=total%1000000007

    return total
        

ls=[11,12, 13]
solve(ls,0, len(ls)-1)




        
    
