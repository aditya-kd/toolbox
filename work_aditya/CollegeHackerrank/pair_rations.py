
def fairRations(B):
    # Write your code here
    odds=0
    oddpos=[False]*len(B)
    index=0
    for num in B:
        if num%2!=0:
            odds+=1
            oddpos[index]=True
        index+=1
    print(oddpos)
    if odds%2!=0:
        return "NO"
    else:
        total=0
        paircomplete=False
        
        for i in range(len(B)):
            if oddpos[i]==True:
                if paircomplete==False:
                    start=i
                    paircomplete=True
                    
                else:
                    total+= i-start
                    paircomplete = False
        return str(total*2)