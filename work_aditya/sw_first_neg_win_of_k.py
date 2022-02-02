def first_negative(arr, n, k):
    ans=[]
    neg=[]
    i,j=0,0

    while j<n:
        if arr[j]<0:
            neg.append(arr[j])

        if j-i+1 < k:
            j+=1
        elif j-i+1 == k:
            if len(neg)==0:
                ans.append(0)
            else:
                ans.append(neg[0])
                if neg[0]==arr[i]:
                    neg.pop(0)
            i+=1
            j+=1
            
            
    print(neg)
    print(ans)

ls=[12,-1,-7,8,-15,30,16,28]
n=len(ls)
k=3
first_negative(ls, n, k)





