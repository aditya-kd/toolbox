
def lilysHomework(A):
    # Write your code here
    swap1,swap2 = 0,0
    d1,d2 = {},{}
    C = A[:]
    S = sorted(A)
    for i,val in enumerate(A): #index, value
        d1[val] = i
        d2[val] = i
    for i in range(len(C)):
        j = d1[S[i]]
        if i!=j:
            swap1+=1
            C[i],C[j] = C[j],C[i]
            d1[C[j]] = j
    C = A[:]
    S = sorted(A,reverse=True)
    for i in range(len(C)):
        j = d2[S[i]]
        if i!=j:
            swap2+=1
            C[i],C[j] = C[j],C[i]
            d2[C[j]] = j
    return min(swap1,swap2)