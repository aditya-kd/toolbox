n,k,q=map(int, input().split())
arr=list(map(int, input().split()))
print(arr)
ans=[]
for i in range(0, n):
    index=(i+k)%n
    print(arr[index])






