from heapq import *
def sortFreq(string):
    fr_map=dict()
    for char in string:
        fr_map[char]=fr_map.get(char,0)+1
    print('frequency: ',fr_map)
    max_heap=[]
    for char, freq in fr_map.items():
        heappush(max_heap, (-freq, char))
    print(max_heap)

    result=[]
    while max_heap:
        freq, char =heappop(max_heap)
        for i in range(-freq):
            result.append(char)
    return ''.join(result) 

print(sortFreq('leetcode'))

