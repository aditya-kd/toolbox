def largestRectangle(h):
    # Write your code here
    # Write your code here
    largest = float("-inf")
    for i in range(0,len(h)):
        j=i
        k=i
        l=-1
        r=len(h)
        while(j>=0):
            if(h[j]<h[i]):
                l=j
                break
            j-=1

        while(k<len(h)):
            if(h[k]<h[i]):
                r=k
                break
            k+=1
        largest = max(largest,(r-l-1)*h[i])
    return largest
