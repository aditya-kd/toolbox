def union(arr1, arr2, n, m):
    freq = {}
    union = []
    for item in arr1:
        freq[item] = freq.get(item, 0)+1
    for item in arr2:
        freq[item] = freq.get(item, 0)+1
    #we have now stored the frequency of elements of each array
    for it in freq.keys():
        union.append(it)
    return union

def main():
    arr1=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    arr2=[ 2, 3, 4, 4, 5, 11, 12 ]
    n = len( arr1 )
    m = len( arr2 )
    print( union(arr1, arr2, n, m) )

main()



