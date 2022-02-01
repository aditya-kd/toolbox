def subst(ss):
    n= len(ss)

    for i in range(n):
        for j in range(i+1, n+1):
            print(ss[i:j])



subst('aditya')

