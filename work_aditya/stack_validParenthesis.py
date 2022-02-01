def matches(a, b):
        if a=='(' and b==')': return True
        elif a=='[' and b==']': return True
        elif a=='{' and b=='}': return True
        else:
            return False

def isValidParenthesis(s):
    stack=[]
    for i in s:
        if i in ['(','{','[']:
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