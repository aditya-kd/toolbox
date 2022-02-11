class Solution:
    def revfunc(self, i,j, s):
        if i>=j:
            return 
        else:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
            self.revfunc(i,j,s)
            
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        return self.revfunc(0,len(s)-1, s)

s=Solution()
instr=list('Aditya')
s.reverseString((instr))
print(instr)

