def solve(name, type):

    if len(name)>len(type):
        return False
    i=0
    j=0
    while i<len(name) and j< len(type):
        if name[i]==type[j]:
            i+=1
            j+=1
        elif i>0 and name[i-1]==type[j]:
            j+=1
        else:
            return False
    while j<len(type):
        if name[i-1]!=type[j]:
            return False
        j+=1

    if  i<len(name):
        return False
    else:
        return True
    


