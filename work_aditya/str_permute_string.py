# not the actual code, needs to be correctly implemented.

def solve(string, left, right):
    if left == right:
        print(''.join(string))
    for i in range(left, right):
        string[left],string[i]=string[i],string[left]
        solve(string, left+1, right)
        string[left], string[i]=string[i],string[left]


def permute(string):
    solve(list(string), 0, len(string)-1)

if __name__ == "__main__":
    string = input()
    permute(string)
