#create a graph and display it
from collections import deque


class Graph:
    
    def __init__(self, vertices):
        self.vertices= vertices
        self.adjacency_list = [[] for i in range(vertices)]
    
    def add_edges(self, source, destination):
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)#only for undirected

    def display(self):
        for vertex in range(len(self.adjacency_list)):
            print(vertex,self.adjacency_list[vertex])

    def bfsComponent(self, vertex, visited, bfs_ans):
        visited[vertex]=True
        q= deque()
        q.append(vertex)
        while len(q)>0:
            u= q.popleft()
            bfs_ans.append(u)
            for v in self.adjacency_list [u]:
                if not visited[v]:
                    visited[v]=True
                    q.append(v)   
                    # print(v)     

    def bfsGraph(self):
        visited=[False]*self.vertices
        bfs_ans = []
        for vertex in range(self.vertices):
            if not visited[vertex]:        
                # print(vertex)        
                self.bfsComponent(vertex, visited, bfs_ans)
        return bfs_ans    


g=Graph(4)
g.add_edges(0,1)
g.add_edges(1,2)
g.add_edges(3,0)
# g.display()
print(g.bfsGraph())
            
