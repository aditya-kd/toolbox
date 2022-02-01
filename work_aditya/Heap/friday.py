from heapq import *
# def question(string):
#     mp={}
#     for char in string:
#         mp[char]=mp.get(char,0)+1
#     max_heap=[]
#     for char, freq in mp.items():
#         heappush(max_heap, (-freq, char))
    
#     prev=None
#     prevFreq=None
#     result=[]
#     while max_heap:
#         curFreq,curChar= heappop(max_heap )
#         curFreq=-(curFreq)
#         result.append(curChar)
#         if prev!=None and prevFreq>0:
#             heappush(max_heap, (-(prevFreq-1),prev))

#         prevFreq=curFreq-1
#         prev=curChar

#     if len(result)==len(string):
#         return ''.join(result)
#     else:
#         return ""



# string='aab'
# print(question(string))

from collections import deque

def reorganizeString(s, k) -> str:
        hash_map = {}
        
        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1
            
        max_heap = []
        
        for char, freq in hash_map.items():
            heappush(max_heap, (-freq, char))
            
        prev_char = None
        prev_freq = None
        
        res = []
        queue=deque()
        while max_heap:
            freq, ch=heappop(max_heap)
            res.append(ch)
            queue.append((ch,freq+1))
            if len(queue)==k:
                c,f=queue.popleft()
                if -f>0:
                    heappush(max_heap, (f,c))

        return ''.join(res) if len(res) ==len(s) else "" 
                
                

            
            # if prev_char is not None and prev_freq > 0:
            #     heappush(max_heap, (-prev_freq, prev_char))
            
            # prev_char = curr_char
            # prev_freq = curr_freq - 1
        
        

s='aabbcc'
k=3
print(reorganizeString(s, k))
s='aaabc'
k=3
print(reorganizeString(s, k))
s='aaadbbcc'
k=2
print(reorganizeString(s, k))


