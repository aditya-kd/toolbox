def reverse0(arr, n):
    copy = []
    #reverse loop 
    for i in range(n-1, -1, -1):
        copy.append(arr[i])
    
    return copy

def reverse1(arr, n):
    start = 0
    end = n-1
    while start<end:
        #swap
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

        start+=1
        end-=1

    return arr

ls = [1,2,3,4,5]
# ls = [1,2,3,4]
# ls = [1,2]
# ls = [1]
n = len(ls)
print(reverse0(ls, n))
# print(reverse1(ls, n))
