def reverseVowels( ss):
        vowels='aeiouAEIOU'
        s=list(ss)
        i=0
        j=len(s)-1
        new_str=['']*len(ss)
        while(i<j):
            if s[i] in vowels and s[j] in vowels:
                new_str[i]=s[j]
                new_str[j]=s[i]
            else:
                new_str[i]=s[i]
                new_str[j]=s[j]
            i+=1
            j-=1
        print(new_str)
                
s='hello'
print(reverseVowels(s))