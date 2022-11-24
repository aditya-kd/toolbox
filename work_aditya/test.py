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
# from heapq import *
# def kthfrequent(arr, k):
#     mp={}
#     for i in arr:
#         mp[i]= mp.get(i,0)+1

#     print('frequency', mp)
#     #create heap
#     max_heap=[]
#     for item in mp.items():
#         fr= item[1]
#         ele= item[0]
#         # print(ele, fr)
#         heappush(max_heap, (-fr, ele))
    
#     print(max_heap)
#     #pop k-1 times to reach kth frequent
#     for i in range(0,k-1):
#         heappop(max_heap)

#     print('Kth Frequent', max_heap[0][1])



# k=2
# arr=[2,2,1,1,1,3,3,4,1,1,1,1,2,2,2,3,3,3,2]
# kthfrequent(arr, k)
# def merge(arr, l, m, r):
#     n1= m-l+1
#     n2= r-m
#     left=[0]*n1
#     right=[0]*n2
#     for i in range(n1):
#         left[i]=arr[l+i]
#     for j in range(n2):
#         right[j] = arr[m+1+j]
#     i=0
#     j=0
#     k=l
#     while i<n1 and j< n2:
#         if left[i]<=right[j]:
#             arr[k]=left[i]
#             i+=1
#         else:
#             arr[k]=right[j]
#             j+=1
#         k+=1
#     while j< n2:
#         arr[k]= right[j]
#         j+=1
#         k+=1
#     while i<n1:
#         arr[k]= left[i]
#         i+=1
#         k+=1

# def mergeSort(arr, l, r):
# 	if l < r:
# 		m = l+(r-l)//2
# 		mergeSort(arr, l, m)
# 		mergeSort(arr, m+1, r)
# 		merge(arr, l, m, r)

# arr=[10,8,9,6,7,5,4,3,2,1]
# n=len(arr)
# mergeSort(arr, 0, n-1)
# print(arr)
# def partition(arr, l, r):
#     pivot= arr[r]
#     i = l - 1
#     for j in range(l, r):
#         if arr[j] <= pivot:
#             i+=1
#             (arr[i],arr[j]) = (arr[j],arr[i])
#     arr[i+1], arr[r] = arr[r], arr[i+1]

#     return i+1
# def quicksort(arr, l, r):
#     if l<r :
#         p= partition(arr,l,r)
#         quicksort(arr, l, p-1)
#         quicksort(arr, p+1, r)
    
# arr=[78,-90,45,23,34,11,12]
# n=len(arr)
# quicksort(arr, 0, n-1)
# print("Quicksort output", arr)
# def partition(arr, l, r):
#     pivot= arr[r]
#     i = l-1
#     for j in range(l, r):
#         if arr[j]<=pivot:
#             i+=1
#             arr[i],arr[j]=arr[j],arr[i]

#     arr[i+1],arr[r]=arr[r],arr[i+1]
#     return i+1

# def quicksort(arr, l, r):
#     if l<r:
#         p= partition(arr,l,r)
#         quicksort(arr, l, p-1)
#         quicksort(arr, p+1,r)
# def partition(arr, l, r):
#     pivot= arr[r]
#     i=l-1
#     for j in range(l,r):
#         if arr[j]<= pivot:
#             i+=1
#             arr[i],arr[j]=arr[j],arr[i]
#     arr[i+1],arr[r]=arr[r],arr[i+1] 
#     return i+1

# def quickselect(arr, l, r,k):
#     idx= partition(arr, l, r)
#     if idx-l == k-1:
#         return arr[idx]
#     elif idx-l > k-1:
#         return quickselect(arr,l,idx-1,k)
#     return quickselect(arr, idx+1, r,k)
# arr=[78, -90, 45, 23, 34, 11, 12]
# n=len(arr)
# print(quickselect(arr,0,n-1, 3))
# print(quickselect(arr,0,n-1, 1))
# print(quickselect(arr,0,n-1, 2))
# from heapq import *
# arr=[120,14040,505,8070,60,90,100]
# max_heap=[]
# for i in arr:
#     heappush(max_heap, -i)

# heappop(max_heap)
# heappop(max_heap)

# print(max_heap)

# mp={}
# for i in range(10):
#     mp[i]=mp.get(i, [])+[12]
# print(mp)

#implementing a stack
# class Stack:
    
#     def __init__(self, size):
#         self.size=size
#         self.element=[0]*size
#         self.top=-1

#     def push(self, value):
#         if self.top==self.size-1:
#             print("Stack Overflow")
#             return
#         else:
#             self.top+=1
#             self.element[self.top]=value
        
#     def pop(self):
#         if len(self.element)==0:
#             print("Stack Underflow")
#             return None
        
#         value = self.element.pop()
#         self.top-=1
#         return value

#     def display(self):
#         print("Stack from bottom to top->")
#         print(self.element[:self.top+1])
    

# stack = Stack(5)
# stack.push(56)
# stack.push(45)
# stack.push(23)
# stack.push(10)
# stack.display()
# stack.push(56)
# stack.push(45)
# stack.display()
# stack.pop()
# stack.pop()
# stack.display()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.display()

#implememtation of Queue
# class Queue:
#     def __init__(self, size):
#         self.size=size
#         self.element=[0]*size
#         self.rear=-1
#         self.front=0
    
#     def push(self, value):
#         if self.rear == self.size-1:
#             print("Queue Overflow")
#         self.rear+=1
#         self.element[self.rear]=value
        
    
#     def pop(self):
#         if self.front==self.rear:
#             print("Queue Empty")
#         value = self.element.pop(0)
#         self.front+=1
#         print("Popped:",value)
#         return value

#     def display(self):
#         print("Queue from FRONT to REAR->")
#         print(self.element[:self.rear+1])

# queue = Queue(5)
# queue.push(56)
# queue.display()
# queue.push(12)
# queue.display()
# queue.push(23)
# queue.push(67)
# queue.push(89)
# queue.display()
# queue.pop()
# queue.pop()
# queue.pop()
# # queue.display()

# class Node:
#     def __init__(self, data):
#         self.data=data
#         self.next= None
    
# class LinkedList:
#     def __init__(self):
#         self.head=None
    
#     def add(self, value):
#         node = Node(value)
#         #list is empty
#         if self.head==None:
#             self.head= node
#         else:
#             temp = self.head
#             while temp.next!=None:
#                 temp=temp.next
#             temp.next= node
    
#     def deleteFromBegin(self):
#         temp= self.head
#         self.head= self.head.next
#         del(temp)
#     def deleteFromLast(self):
#         if self.head.next==None:
#             self.head=None
#             return
#         temp= self.head
#         while temp.next.next !=None:
#             temp = temp.next
#         temp.next= None

#     def display(self):
#         if self.head==None:
#             print("Empyt List")
#             return
#         temp= self.head
#         while temp !=None:
#             print(temp.data,'-> ', end='')
#             temp=temp.next
#         print('X')
    
#     def sort(self):
#         if self.head==None:
#             return None
#         current= self.head
#         while current.next!=None:
#             index = current.next
#             while index!=None:
#                 if current.data > index.data:
#                     #swap them
#                     temp = current.data
#                     current.data = index.data
#                     index.data = temp
#                 index = index.next

#             current = current.next

    

# mylist = LinkedList()
# mylist.add(56)
# mylist.add(34)
# mylist.add(90)
# mylist.add(2)
# mylist.add(10)
# mylist.add(-89)
# mylist.display()
# # mylist.deleteFromBegin()
# # mylist.display()
# # mylist.deleteFromLast()
# # mylist.deleteFromLast()
# # mylist.display()
# print("After Sorting")

# mylist.sort()
# mylist.display()

# from collections import deque
# from turtle import Turtle
# from types import TracebackType

# class Graph:
#     def __init__(self, vtx):
#         self.vertices=vtx
#         self.adjacencyList= [[] for i in range(vtx+1)]

#     def addEdges(self, source, dest):
#         self.adjacencyList[source].append(dest)
#         self.adjacencyList[dest].append(source)#undirected graph

#     def display(self):

#         for vertex in range(1, len(self.adjacencyList)):
#             print('Node',vertex,':',self.adjacencyList[vertex])

#     #BREADTH FIRST TRAVERSAL
#     def bfs(self, src):
#         bfs=[]#storing BFS nodes as answer
#         queue= deque()
#         visited = [False]*(self.vertices+1)

#         queue.append(src)
#         visited[src]=True

#         while len(queue)!=0:
#             currnode = queue.popleft()
#             bfs.append(currnode)

#             for neighbour in self.adjacencyList[currnode]:
#                 if visited[neighbour] == False:
#                     queue.append(neighbour)
#                     visited[neighbour]=True
                
#         return bfs
    
#     def dfs_helper(self, vertex, visited, dfs):
#         visited[vertex]=True
#         dfs.append(vertex)
#         for vtx in self.adjacencyList[vertex]:
#             if visited[vtx] == False:
#                 self.dfs_helper(vtx, visited, dfs)

#     def dfs(self, src):
#         dfs=[]
#         visited = [False]*(self.vertices+1)
#         #initialize
#         dfs.append(src)
#         visited[src]=True
#         for neighbour in self.adjacencyList[src]:
#             if visited[neighbour] == False:
#                 self.dfs_helper(neighbour, visited, dfs)

#         return dfs






# edges=[[1,2],[3,2],[1,4],[2,5],[3,5],[4,5]]
# graph= Graph(5)
# for edge in edges:
#     src = edge[0]
#     dest = edge[1]
#     graph.addEdges(src, dest)

# graph.display()

# bfs_traversal=graph.bfs(1)
# print("BFS: ",bfs_traversal)

# dfs_traversal= graph.dfs(1)
# print("DFS: ", dfs_traversal)




    



# # Python3 code for First negative integer
# # in every window of size k
# def printFirstNegativeInteger(arr, k):
# 	firstn = 0

# 	for i in range(k - 1, len(arr)):

# 		while firstn < i and (firstn <= i - k or arr[firstn] >= 0):
# 			firstn += 1

# 		firstNegativeElement = arr[firstn] if arr[firstn] < 0 else 0
# 		print(firstNegativeElement, end=' ')


# arr = [-11,-2, 19,37,64,-18]
# k = 3
# printFirstNegativeInteger(arr, k)
	

# # contributed by Arjun Lather



# class Solution(object):
#     def setZeroes(self, matrix):
       
#         is_col = False
#         R = len(matrix)
#         C = len(matrix[0])
#         for i in range(R):
           
#             if matrix[i][0] == 0:
#                 is_col = True
#             for j in range(1, C):
#                 if matrix[i][j]  == 0:
#                     matrix[0][j] = 0
#                     matrix[i][0] = 0

#         for i in range(1, R):
#             for j in range(1, C):
#                 if not matrix[i][0] or not matrix[0][j]:
#                     matrix[i][j] = 0

#         if matrix[0][0] == 0:
#             for j in range(C):
#                 matrix[0][j] = 0

#         if is_col:
#             for i in range(R):
#                 matrix[i][0] = 0
# 
# def merge(arr, l, m, r):
#     n1 = m-l+1
#     n2 = r-m
#     left = [0]*n1
#     right = [0]*n2
#     #fill first array
#     for i in range(n1):
#         left[i] = arr[l+i]
#     #fill right arrray
#     for j in range(n2):
#         right[j] = arr[m+j+1]
    
#     i=0
#     j=0
#     k=l
#     while i<n1 and j<n2:
#         if left[i] < right[j]:
#             arr[k] = left[i]
#             i+=1
#         else:
#             arr[k] = right[j]
#             j+=1
#         k+=1
    
#     while i<n1:
#         arr[k] = left[i]
#         i+=1
#         k+=1
#     #fill second array
#     while j<n2:
#         arr[k] = right[j]
#         j+=1
#         k+=1
    
# def mergesort(arr, l, r):
#     if l<=r:
#         mid= l+(r-l)//2
#         mergesort(arr, l, mid)
#         #count inversion
#         mergesort(arr, mid+1, r)
#         #count inversion
#         merge(arr, l, mid, r)


# def reverse(head):
#     curr=head
#     prev=None
#     next=None
#     while curr!=None:
#         next=curr.next
#         curr.next=prev
#         prev=curr
#         curr=next
#     return prev


# def solve(head, left, right):

#     temp=head
#     copy = head
#     curhead = temp
#     while temp.val != right or temp.next!=None:
#         if temp.next.val == left.val:
#             curhead = temp
#         temp = temp.next
#     curtailhead = temp.next
#     curtail = temp
#     curhead.next = reverse(curhead.next, curtail)
    


# Python3 program to Check if given string can
# be formed by concatenating string elements
# of list

# Function to check string can be formed using list or not
# def checkList(str1, input2):
#     list1=list(map(str, input2.split(' ')))

#     for i in list1:
# 		# Replacing the sub-string from string
# 	    str1 = str1.replace(i, "")
# 		# Checking the emptiness of string
# 	    if str1 == "":
# 		    return True
			
# 	# Else returning False
# 	else: return False
	
# # Driver code
# str = 'codeit'
# lst = 'code it'
# print(checkList(str, lst))

    

# def prakhar(arr1, arr2):
#         n = len(arr1)
#         dp = [-1] * (1 << n)  
#         def calculate(i, mask):
#             if i == n: 
#                 return 0
            
#             if dp[mask] != -1:
#                 return dp[mask]
            
#             ans = float('inf')
#             for j in range(n):
#                 if (mask & 1 << j) == 0: # check for unused element
#                     ans = min(ans, (arr1[i]^arr2[j]) + calculate(i+1, mask | (1 << j))) 
#             .
#             dp[mask] = ans
#             return dp[mask]
#         return calculate(0, 0)

# n= int(input())
# arr1=list(map(int, input().split()))
# arr2=list(map(int, input().split()))
# print(prakhar(arr1, arr2))

# Python3 implementation of above approach

# Function to return sum of width of all subsets
# def SubseqWidths(A):
# 	MOD = 10**9 + 7
# 	N = len(A)
# 	A.sort()

# 	pow2 = [1]
# 	for i in range(1, N):
# 		pow2.append(pow2[-1] * 2 % MOD)

# 	ans = 0
# 	for i, x in enumerate(A):
# 		ans = (ans + (pow2[i] - pow2[N - 1 - i]) * x) % MOD
# 	return ans


# # Driver program
# A = [5, 6, 4, 3, 8]

# print(SubseqWidths(A))

# def longestNonDecreasingSubsequence(self, arr):
#         sub = []
#         for i, x in enumerate(arr):
#             if len(sub) == 0 or sub[-1] <= x:  
#                 sub.append(x)
#             else:
#                 idx = bisect_right(sub, x)  # Find the index of the smallest number > x
#                 sub[idx] = x  # Replace that number with x
#         return len(sub)


# n,k=map(int,input().split())

# s=list(map(int,input().split()))

# sum=0

# t=[]

# mad=[]

# for i in range(k):

#     sum+=s[i]

#     t.append(s[i])

#     mad.append(sum)

# for i in range(k-1):

#     sum= sum -t[len(t)-1-i]+ s[len(s)-1-i]

#     mad.append(sum)

# print(max(mad))


# # def solve(k, inarr):
# #     temp = []
# #     mad
# # size, k = map(int,input().split())
# # inarr = list(map(int, input().split()))



# n, qrs = map(int, input().split())
# items = list(map(int, input().split()))

# Python3 program to find the number
# of elements in a range L to R having
# the Kth bit as set

# Maximum bits required in binary
# representation of an array element
# MAX_BITS = 32

# # Returns true if n has its kth
# # bit as set,else returns false
# def isKthBitSet(n, k):
# 	if (n & (1 << (k - 1))):
# 		return True
		
# 	return False

# # Return pointer to the prefix sum array
# def buildPrefixArray(N, arr):
	
# 	# Build a prefix sum array P[][]
# 	# where P[i][j] represents the
# 	# number of elements from 0 to
# 	# i having the jth bit as set
# 	P = [[0 for i in range(MAX_BITS + 1)]
# 			for i in range(N + 1)]

# 	for i in range(N):
# 		for j in range(1, MAX_BITS + 1):
			
# 			# prefix sum from 0 to i for each bit
# 			# position jhas the value of sum from 0
# 			# to i-1 for each j
# 			if (i):
# 				P[i][j] = P[i - 1][j]

# 			# If jth bit set then increment
# 			# P[i][j] by 1
# 			isJthBitSet = isKthBitSet(arr[i], j)
			
# 			if (isJthBitSet):
# 				P[i][j] += 1

# 	return P


# def answerQuery(L, R, K, P):

# 	# Number of elements in range L to
# 	# R with Kth bit set = (Number of
# 	# elements from 0 to R with kth
# 	# bit set) - (Number of elements
# 	# from 0 to L-1 with kth bit set)
# 	if (L):
# 		return P[R][K] - P[L - 1][K]
# 	else:
# 		return P[R][K]

# # Print the answer for all queries
# def answerQueries(queries, Q, arr, N):

# 	# Build Prefix Array to answer
# 	# queries efficiently
# 	P = buildPrefixArray(N, arr)

# 	for i in range(Q):
# 		query_L = queries[i][0] - 1
# 		query_R = queries[i][1] - 1
# 		query_K = queries[i][2]

# 		print("Result for Query ", i + 1,
# 			" = ", answerQuery(query_L, query_R,
# 								query_K, P))

# # Driver Code
# if __name__ == '__main__':

# 	arr = [ 8, 9, 1, 3 ]
# 	N = len(arr)

# 	# queries[]denotes the array of queries
# 	# where each query has three integers
# 	# query[i][0] -> Value of L for ith query
# 	# query[i][0] -> Value of R for ith query
# 	# query[i][0] -> Value of K for ith query
# 	queries = [ [ 1, 3, 4 ],
# 				[ 2, 4, 1 ] ]
				
# 	Q = len(queries)

# 	answerQueries(queries, Q, arr, N)

# # This code is contributed by mohit kumar 29


# def solve(arr, k):
# 	for i in range(0, k-1):
# 		print(arr[i])

# This is a happy house123
# 0123456789...


# house 
# esuoh
# house
# def reverseSentence(sentence):

#     sentence = sentence+" "
#     stack = []
#     word = ''
#     for i in range(0, len(sentence)):

#         letter = sentence[i]
#         # letter is whitespace
#         if letter == ' ':
#             # new word
#             stack.append(word)
#             word = ''
#         else:
#             word = word + letter
        
#     while len(stack) != 0:
#         word = stack.pop()
#         print(word, end=' ')
    
#     print()
        

# inputstr = input()
# reverseSentence(inputstr)
print('Enter vertices and edges')
vertices = 6
edges = 6
print('Edge: ', edges, 'Vertices: ', vertices)
# vertices = int(input())
# edges = int(input())
edgelist=[]
edgelist = [[1,4],[1,2],[1,3],[4,3],[3,5]]
edgelist = [[1,2], [1,4], [1,3], [2,6], [4,5], [5,3], [6,5]]
print("Edge List")
adjList = [[] for i in range(vertices+1)]

#accepting edges
# for i in range(edges):
#     u,v = map(int, input().split())
#     edgelist.append([u,v])

def addEdge(source, destination):
    #directed 
    adjList[source].append(destination)
    #undirected
    adjList[destination].append(source)


def createGraph(vertices, edges, edgelist):
    for e in edgelist:
        u = e[0]
        v = e[1]
        addEdge(u,v)

def displayGraph():
    for vtx in range(len(adjList)):
        print(vtx, adjList[vtx])

from collections import deque
def bfs(source):
    bfs = []
    queue = deque()
    visited = [False] * (vertices+1)
    #process source
    queue.append(source)
    visited[source] = True

    while len(queue)!=0:
        currNode = queue.popleft()
        bfs.append(currNode)

        for nbr in adjList[currNode]:
            if visited[nbr] == False:
                queue.append(nbr)
                visited[nbr] = True

    return bfs

def dfs_recurse(node, visited, dfs):
    dfs.append(node)
    visited[node] = True
    for nbr in adjList[node]:
        if visited[nbr] == False:
            dfs_recurse(nbr, visited, dfs)

def dfs(source):
    dfs = []
    visited = [False] *(vertices+1)

    dfs.append(source)
    visited[source] = True

    for nbr in adjList[source]:
        if visited[nbr] == False:
            dfs_recurse(nbr, visited, dfs)
    return dfs

#only for dag
# toposort using DFS
def topoHelper(source, visited, stack):
    visited[source] = True
    for node in adjList[source]:
        if visited[node] == False:
            topoHelper(node, visited, stack)

    stack.append(source)
    return stack[-1::-1]
def topoSort(source):
    visited = [False]*(vertices+1)
    stack = []
    return topoHelper(source, visited, stack)

# Topo Sort using BFS
# uses indegree
def topoSortBFS():
    topo = []
    indegree = [0]*(vertices+1)
    for t in range(0,vertices+1):
        for i in adjList[t]:
            indegree[i] += 1

    print("Indegree:",indegree)
    queue = deque()
    for vtx in range(0,vertices+1):
        if indegree[vtx] == 0:
            queue.append(vtx)
    print("queue", queue)
    ind = 0
    while len(queue)>0:
        node = queue.popleft()
        print("node popped: ", node)
        topo.append(node)

        for nbr in adjList[node]:
            indegree[nbr] =- 1
            if indegree[nbr] == 0:
                queue.append(nbr)

    return topo
      

def main():
    createGraph(vertices, edges, edgelist)
    displayGraph()
    print("Performing BFS")
    source = 1
    print(bfs(source))
    print(dfs(source))
    print(topoSort(source))
    print(topoSortBFS())


main()


    




    


        




    












            
        




		



