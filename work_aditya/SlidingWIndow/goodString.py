def goodString(arr):
    s=0
    e=2
    while e<len(arr):
        print(arr[s:e+1])
        s+=1
        e+=1

goodString('aababcabc')