class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count=[0]*128
        for ch in s:
            char_count[ord(ch)]+=1
        
        result=0
        for cha_count in char_count:
            result+= (cha_count//2)*2
            if result%2==0 and cha_count%2==1:
                result+= 1
                
        return result