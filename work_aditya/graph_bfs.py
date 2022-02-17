from collections import deque
class Graph:
    
    def __init__(self, vertices):
        self.vertices= vertices
        self.adjacency_list = [[] for i in range(vertices)]
    
    def add_edges(self, source, destination):
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)#only for undirected
    
    def gridToAdjacencyList(vertices, edges):
        d = dict()
    # initializing the graph (converting edges into an adjacency list)
        for i in range(1, vertices + 1):
            d[i] = list()
        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        return d

    def display(self):
        for vertex in range(len(self.adjacency_list)):
            print(vertex,self.adjacency_list[vertex])

    def bfs(self, source):
        bfs=[]
        queue = deque()
        visited = [False]*self.vertices
        #initiate
        queue.append(source)
        visited[source]=True

        while len(queue)!=0:
            currNode= queue.popleft()
            bfs.append(currNode)
            #till here it is standard code to pop node
            #calculations from now on.
            for neighbour in self.adjacency_list[currNode]:
                if visited[neighbour] == False:
                    queue.append(neighbour)
                    visited[neighbour]=True
        return bfs

    def dfs_recursive(self, node, visited, dfs_ans):
        dfs_ans.append(node)
        visited[node]= True
        for neighbour in self.adjacency_list[node]:
            if not visited[neighbour]:
                self.dfs_recursive(neighbour, visited, dfs_ans)

    def dfs(self, source):
        dfs_ans=[]
        visited=[False]*(self.vertices+1)
        dfs_ans.append(source)
        visited[source]=True
        for vertex in self.adjacency_list[source]:
            if not visited[vertex]:
                self.dfs_recursive(vertex, visited, dfs_ans)

        return dfs_ans    
    # def bfsComponent(self, vertex, visited, bfs_ans):
    #     visited[vertex]=True
    #     q= deque()
    #     q.append(vertex)
    #     bfs_ans.append(vertex)
    #     while len(q)>0:
    #         u= q.popleft()
    #         bfs_ans.append(u)
    #         for v in self.adjacency_list [u]:
    #             if not visited[v]:
    #                 visited[v]=True
    #                 q.append(v) 
    #                 # bfs_ans.append(v) 

    # def bfsGraph(self,source):
    #     visited=[False]*self.vertices
    #     bfs_ans = []
    #     visited[source]=True
    #     bfs_ans.append(source)
    #     for vertex in self.adjacency_list[source]:
    #         if not visited[vertex]:        
    #             self.bfsComponent(vertex, visited, bfs_ans)
    #     return bfs_ans  

    
    
g=Graph(4)
g.add_edges(0,1)
g.add_edges(1,2)
g.add_edges(3,0)
g.display()
print(g.bfs(0))
print(g.bfsGraph(0))
# print(g.dfs(3))
            
