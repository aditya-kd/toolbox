def nser( arr, n):
        s=[]
        ans=[-1]*n
        
        for i in range(n-1, -1, -1):
            while len(s)>0 and s[-1][0]>=arr[i]:
                s.pop()
                
            if len(s)==0:
                ans[i]=n
            else:
                ans[i]=s[-1][1]
            
            s.append([arr[i], i])
        return ans
    
def nsel( arr, n):
        s=[]
        ans=[-1]*n
        
        for i in range(n):
            
            while len(s)>0 and s[-1][0]>=arr[i]:
                s.pop()
            if len(s)==0:
                ans[i]=-1
            else:
                ans[i]=s[-1][1]
            s.append([arr[i], i])
            
        return ans
    
def largestRectangleArea( heights):
        n=len(heights)
        sel = nsel(heights, n)
        ser = nser(heights, n)
        print(sel)
        print(ser)
        ans=[]
        area= -950934
        for i in range(n):
            a = (ser[i] - sel[i] -1)*heights[i]
            ans.append(a)
            if area<= a:
                area=a

        print(ans)
        print(area)
                
        return area
        
        
ls=[2,1,5,6,2,3]
# ls=[6,2,5,4,5,1,6]

largestRectangleArea(ls)