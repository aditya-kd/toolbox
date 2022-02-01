def solve(output, op, cl, ans):
    if op==0 and cl==0:
        ans.append(output)
        return 
    if op!=0 and op< cl:
        solve(output+ '(', op-1, cl, ans)
        solve(output+ ')', op, cl-1 ,ans)
    else:
        if op==0:
            solve(output+')', op, cl-1, ans)
        if op==cl:
            solve(output +'(',op-1, cl, ans)
        
class Solution:
    def generateParenthesis(self, n: int) :
        ans=[]
        solve('', n,n, ans)
        return ans
        