# Online Python compiler (interpreter) to run Python online.
l = int(input()) 
r = int(input()) 
a = int(input()) 
b = int(input()) 
c = 0
for i in range(l*2, r*2) :
    if i%a == 0 and i%b == 0:
        g = str(i) 
        if str(a) in g and str(b) in g:
            c+=1
print(c)
