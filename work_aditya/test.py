# # from itertools import chain, combinations

# # def power(iterable) :
# #   s = list(iterable)
# #   return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

# # n = int(input())
# # match = input().split(",")
# # string = input().split(",")

# # subsets = list(power(string))

# # for i,j in enumerate(subsets) :
# #   if list(j) == match :
# #     print(i+1)
# #     break

# class Solution:
#     def threeSumMulti(self, A, target):

#         mod= 10**9+7
#         count= [0]*101
#         for x in A:
#             count[x]+=1

#         ans=0

#         for x in range(101):
#             z= target-2*x
#             if x<z and z<=100:
#                 ans+= count[x]*(count[x]-1)/2*count[z]
#                 ans%=mod

#         for x in range(101):
#             if (target-x)%2==0:
#                 y= (target-x)/2
#                 if x<y and y<=100:
#                     ans+= (count[x]*count[y]*(count[y]-1))/2
#                     ans%= mod

#         if target%3==0:
#             x=target/3
#             if 0<= x and x<= 100:
#                 ans+= count[x]*(count[x]-1)*(count[x]-2)/2
#                 ans%= mod

#         return ans
    
        

# def find(v, parent):
   
#     if v!=parent[v]: parent[v]= find(parent[v], parent)
#     return parent[v]
    


# def minCost(points):
#     n= len(points)
#     edges=[[]]
#     for i in range(n-1):
#         for j in range(i+1, n):
#             edges.append([
#                 abs(points[i][0]-points[j][0])
#             ,abs(points[i][1] - points[j][1]),
#             i,
#             j])
#     edges.sort()
#     parent=[]*n
#     for i in range(0, n):
#         parent[i]=i
#     result=0
#     edgescount=0

#     for e in range(0, len(edges)):
#         group1= find(edges[e][0], parent)
#         group2= find(edges[e][1], parent)
#         if group1 != group2:
#             parent[group1]=group2

#             result+= edges[e][0]
#             edgescount+=1
#             if (edgescount) == n-1: 
#                 break

#     return result
        

# from heapq import *
# from traceback import print_tb
# min_heap=[]
# li=[('a', 2),('e',3),('f',4),('b',1)]
# # li=[(2,'a'),(3,'e'),(1,'b'),(4,'f')]
# for item in li:
#     heappush(min_heap, item)
# while len(min_heap)>0:
#     print(heappop(min_heap))

# from queue import PriorityQueue
# pq= PriorityQueue()
# # li=[('a', 2),('e',3),('f',4),('b',1)]
# li=[(2,'a'),(3,'e'),(1,'b'),(4,'f')]
# for item in li:
#     pq.put(item)

# while pq.empty()==False:
#     print(pq.get())
# print('hello world')
from heapq import *
def kthfrequent(arr, k):
    mp={}
    for i in arr:
        mp[i]= mp.get(i,0)+1

    print('frequency', mp)
    #create heap
    max_heap=[]
    for item in mp.items():
        fr= item[1]
        ele= item[0]
        # print(ele, fr)
        heappush(max_heap, (-fr, ele))
    
    print(max_heap)
    #pop k-1 times to reach kth frequent
    for i in range(0,k-1):
        heappop(max_heap)

    print('Kth Frequent', max_heap[0][1])



k=2
arr=[2,2,1,1,1,3,3,4,1,1,1,1,2,2,2,3,3,3,2]
kthfrequent(arr, k)









