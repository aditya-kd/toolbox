print('Hello World')
for i in 'hello world':
    print(i)

def genSubarrays(arr):
    n=len(arr)
    for i in range(0, n):
        temp=[]
        for j in range(i, n):
            temp.append(arr[j])
            print(temp)
        temp.clear()

arr=[1,2,3,4,5]
genSubarrays(arr)



