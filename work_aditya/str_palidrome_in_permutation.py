from gettext import find


def findPalindrome(s):
    mp={}
    for ch in s:
        mp[ch]=mp.get(ch, 0)+1
    hasOdd=False
    for freq in mp.values():
        if freq%2==1:
            if hasOdd:
                return False
            else:
                hasOdd=True
    return True

s='aaabbbb'
print(findPalindrome(s))
