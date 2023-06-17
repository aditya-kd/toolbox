# Given MAX Value is 15
def frequency(arr, n):

    freq = [0]*(16)
    for i in range(0, n):
        
        item = arr[i]
        freq[item] +=1 

    return freq

def printFrequency(arr, n):

    freq =  frequency(arr, n)
    for i in range(0, len(freq)):
        if freq[i] != 0:
            print(i,':', freq[i])

    
def frequency2(arr, n):
    
    freq = {}
    for i in range(0, n):

        item = arr[i]
        keys = freq.keys()

        if item in keys:
            freq[item] +=1 
        else:
            freq[item] = 1

    print("Frequency: ", freq)


ls = [1,2,3,4,5,5,5,8,9,10]
ls2= [1,2,6,4,2,3,1,3,4,5,1]
print("Item : Freq")
printFrequency(ls2, len(ls2))
frequency2(ls, len(ls))