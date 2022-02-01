def reverse(n):
    return int(str(n)[::-1])

if __name__=='__main__':
    n = int(input())
    while True:
        if n== reverse(n):
            print(n)
            break
        else:
            k=reverse(n)
            n=k+n
            
