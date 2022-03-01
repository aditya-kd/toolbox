def caesarCipher(s, k):
    # Write your code here
    new_str=''
    for ch in s:
        asci=ord(ch)
        if asci>=65 and asci<=90:
            new_asci=(asci+k)%90
            if new_asci<65:
                new_str+=chr(new_asci+64)
            else:
                new_str+=chr(new_asci)
        elif asci>=97 and asci<=122:
            new_asci=(asci+k)%122
            if new_asci<97:
                new_str+=chr(new_asci+96)
            else:
                new_str+=chr(new_asci)
        else:
            new_str+=ch
    return new_str
            
s='www.abc.xy'
print(caesarCipher(s, 2))

