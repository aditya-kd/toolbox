s='adars123h'
vowels=[]
consonants=[]
v='aeiouAEIOU'
for i in s:

    if i in v:
        vowels.append(i)
    elif i not in v and i not in '1234567890':
        consonants.append(i)

print('vowels: ',vowels)
print('consonants: ', consonants)
    

