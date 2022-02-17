#create a graph and display it
from collections import deque
class Graph:
    
    def __init__(self, vertices):
        self.vertices= vertices+1
        self.adjacency_list = [[] for i in range(vertices+1)]
    
    def add_edges(self, source, destination):
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)#only for undirected

    def display(self):
        for vertex in range(len(self.adjacency_list)):
            print(vertex,self.adjacency_list[vertex])
    def bfs(self, source):
        bfs=[]
        queue = deque([])
        visited = [False]*self.vertices
        queue.append(source)
        visited[source]=True
        while len(queue)!=0:
            currNode= queue.popleft()
            bfs.append(currNode)
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

g=Graph(5)
g.add_edges(1,2)
g.add_edges(2,4)
g.add_edges(2,7)
g.add_edges(4,6)
g.add_edges(7,6)
g.display()
            
