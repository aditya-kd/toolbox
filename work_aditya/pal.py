# not the actual code, needs to be correctly implemented.
import string


palidromes=[]
def isPalindrome(num):
    if num==num[::-1]:
        return True
    else:
        return False

def solve(string, left, right):
    if left == right:
        # print(''.join(string))
        res=''.join(string)
        if isPalindrome((res)):
            palidromes.append(res)
    for i in range(left, right):
        string[left],string[i]=string[i],string[left]
        solve(string, left+1, right)
        string[left], string[i]=string[i],string[left]


def permute(string):
    solve(list(string), 0, len(string)-1)
    # print(palidromes)
    if len(palidromes)==0:
        print(-1)
    else:
        print(max(palidromes))

if __name__ == "__main__":
    string=input()
    permute(string)
