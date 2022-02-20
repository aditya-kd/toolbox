from collections import deque
from queue import PriorityQueue
import sys
from tkinter import N

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
    #CYCLE CHECKING/DETECTION
    #USING BFS UNDIRECTED
    def checkCycle(self, adj, s, vis, parent):
        q=deque()
        q.add((s,-1))
        vis[s]=True
        while len(q)>0:
            node= q[0][0]
            par= q[0][1]
            q.popleft()

            for i in adj[node]:
                if vis[i]==False:
                    q.append((i, node))
                    vis[i]=True
                elif par!=i:
                    return True
        return False
    def isCycle(self, vertices, adjlist): 
        visited=[False]*vertices
        parent=[-1]*vertices
        for i in range(0, vertices):
            if visited[i]==False:
                if self.checkCycle(adjlist, i, visited, parent):
                    return True
        return False
    #Check Cycle DFS UNDIRECTED GRAPH
    def checkForCycle(self, node, parent, vis, adj):
        vis[node]=True
        for i in adj[node]:
            if vis[i]==False:
                if self.checkForCycle(i, node, vis, adj)==True:
                    return True
            elif i!=parent:
                return True
        return False
    def isCycle(self, v, adj):
        vis=[False]*v
        for i in range(0, v):
            if vis[i]==False:
                if self.checkForCycle(i, -1, vis, adj):
                    return True
        return False
    #CHECK CYCLE DFS DIRECTED GRAPH
    def checkDFS(self, node, adj, vis, dfsvis):
        vis[node]=True
        dfsvis[node]=True
        for i in adj[node]:
            if vis[node]==False:
                if self.checkDFS(i, adj, vis, dfsvis)==True:
                    return True
            elif dfsvis[i]==True:
                return True
        dfsvis[node]=False
        return False
    def isCycleDFS(self, vertices, adj):
        vis=[False]*vertices
        dfsvis=[False]*vertices
        for i in range(0, vertices):
            if vis[i]==False:
                if self.checkDFS(i, adj, vis, dfsvis)==True:
                    return True
        return False
    #CHECK CYCLE BFS(KAHN'S ALGORITHM) DIRECTED GRAPH
    #if there is a cycle topo sort won't be successful.
    def isCyclic(vertices, adj):
        q=deque()
        indegree=[0]*vertices
        for i in range(0, vertices):
            for t in adj[i]:
                indegree[t]+=1
        for i in range(0, vertices):
            if indegree[i]==0:
                q.append(i)
        cnt=0
        while len(q)>0:
            node= q.popleft()
            cnt+=1
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        if cnt==vertices:
            return False
        return True
        
    #BIPARTITE BFS
    def bfCheck(self, adj, node, color):
        q=deque()
        q.append(node)
        color[node]=1
        while len(q)>0:
            curr = q.popleft()
            for i in adj[node]:
                if color[i]==-1:
                    color[i]=1-color[node]
                    q.append(i)
                elif color[i]== color[node]:
                    return False
        return True
    def isBipartite(self, adj, vertices):
        color=[-1]*vertices
        for i in range(0, vertices):
            if color[i]==-1:
                if self.bfscheck(adj, i, color):
                    return False

        return True
#Bipartit DFS
    def dfscheck(self, node, vis, adj, dfsans):
        dfsans.append(node)
        vis[node]=True
        for i in adj[node]:
            if vis[i]==False:
                self.dfscheck(i, vis, adj, dfsans)

    def isBipartiteDFS(self, adj, vertices):
        dfsans=[]
        vis=[False]*(vertices+1)
        for i in range(1, vertices+1):
            if vis[i]==False:
                self.dfscheck(i, vis, adj, dfsans)
        return dfsans
        #TOPOLOGICAL SORTING
        #DFS
    def findTopoSort(self, node, vis, adj, st):
        vis[node]=True
        for i in adj[node]:
            if vis[i]==False:
                self.findTopoSort(i, vis, adj,st)
        st.append(node)
    def topoSort(self, vertices, adj):
        st=[]
        vis=[False]*vertices
        for i in range(0, vertices):
            if vis[i] == False:
                self.findTopoSort(self, i, vis, adj, st)

        topo=[]*vertices
        ind =0
        while len(st)>0:
            topo[ind] = st.pop()
            ind+=1
        return topo
    
    #TOPOLOGICAL SORTING BFS(KAHN's ALGORITHM)
    def topoSortBFS(self, vertices, adj):
        topo=[]*vertices
        indegree=[]*vertices
        for i in range(0, vertices):
            for i in adj[i]:
                indegree[i]+=1
        q= deque()
        for i in range(0, vertices):
            if indegree[i]==0:
                q.append(i)
        cnt=0
        ind=0
        while len(q)>0:
            node= q.popleft()
            topo[ind]=node
            ind+=1

            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)

        return topo


    def findNoofPaths(self, src, dest, graph):
        if src==dest:
            return 1
        pathCount=0
        for nbr in graph[src]:
            pathCount+= self.findNoofPaths(nbr, dest, graph)
        return pathCount

    #SHORTEST PATH
    #DFS
    def shortestPathDFS(adj, vertices, src):
        dist=[]*vertices
        for i in range(0, vertices):
            dist[i]= 10000000
        q=deque()
        dist[src] = 0
        q.append(src)

        while len(q)>0:
            node= q.popleft()
            for i in adj[node]:
                if dist[node] +1 < dist[i]:
                    dist[i] = dist[node]+1
                    q.append(i)
        #print result
        print('Shortest Distance for each node')
        for i in range(0, vertices):
            print(i, dist[i],'units')
        return dist
    #TOPO + BFS (DAG)
    def toposort(self, node, vis, adj, st):
        vis[node]= True
        for i in adj[node]:
            self.toposort(i, vis, adj, st)
        st.append(node)

    def shortestPathDAG(self, src, adj, vertices):
        st=[]
        dist=[sys.maxsize]*vertices
        vis=[False]*vertices
        dist[src]=0
        for i in range(0, vertices):
            if vis[i]==False:
                self.toposort(i, vis, adj, st)
        
        while len(st)>0:
            node= st.pop()
            if dist[node]!= sys.maxsize:
                for pair in adj[node]:
                    if dist[node] + pair[1] < dist[pair[0]]:
                        dist[pair[0]] = dist[node] + pair[1]
        return dist
    #DIJKSTRA [Directed/Undirected No -ve weighted]
    def dijkstra(self, src, adj, vertices):
        dist=[sys.maxisze]*vertices
        dist[src]=0
        
        pq= PriorityQueue()
        pq.put((src,0))

        while len(pq)>0:
            node = pq.get()

            for it in adj[node[0]]:
                if dist[node[0]] + it[1] < dist[it[0]]:
                    dist[it[0]] = dist[node[0]] + it[1]
                    pq.put((it[0], dist[it[0]]))
        return dist
    #CONNECTED COMPONENTS
    def countComponents(self, vertices, edges):
        parent= [i for i in range(vertices)]
        rank = [1]*vertices
        
        def find(n1):
            res= n1
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(n1, n2):
            p1, p2= find(n1), find(n2)
            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2]+= rank[p2]
            return 1
        res = vertices
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res#no. of connected components

    
    
g=Graph(4)
g.add_edges(0,1)
g.add_edges(1,2)
g.add_edges(3,0)
g.display()
print(g.bfs(0))
print(g.bfsGraph(0))
# print(g.dfs(3))
            

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