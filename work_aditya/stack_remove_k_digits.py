class Solution:
    def removeKdigits(self, num, k):
        if len(num)==k:
            return str(0)
        stack=[]
        i=0
        while i< len(num) and k>0:
            while k>0 and len(stack) >0 and int(stack[-1]) > int(num[i]):
                stack.pop()
                k-=1
            stack.append(num[i])
            i+=1
        
        while len(stack) >0 and k>0:
            stack.pop()
            k-=1
        ans= ''.join(stack)
        final_ans = ans+num[i:]
        j=0
        while j<len(final_ans):
            if int(final_ans[j])!=0:
                break
            j+=1
        if len(final_ans[j:]) == 0:
            return '0'
        return final_ans[j:]
    
  
                
        
            
