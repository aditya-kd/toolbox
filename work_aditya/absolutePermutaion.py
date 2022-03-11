from itertools import permutations

def absolutePermutation(n, k):
    if k ==0:
        print(*(range(1,n+1)))
    elif (n/k)%2!=0.0:
        print(-1)
    else:
        arr = []
        for i in range(1,n,k*2):
            d = list(range(i, i+k*2)) 
            arr+=d[k:]+d[:k]
        print(*arr)

for _ in range(int(input())):
    n,k = map(int,input().split())
    absolutePermutation(n, k)