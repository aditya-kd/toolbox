from heapq import *
vertices= int(input("Vertices: ?"))
e= int(input("Edges: ?"))
edges=[]
# adjlist=[[]for i in range(vertices)]
#creates edge list with weight
for i in range(e):
    src, dest, wt= tuple(map(int, input().split()))
    edges.append([src, dest,wt])

#creates adj list wihtout weight and matrix along with weight
graph= [ [-1 for i in range(vertices+1)] for j in range(vertices+1)]
for edge in edges:
    src,dest,wt= edge[0], edge[1], edge[2]
    graph[src][dest] = wt

print(graph)
import math
def dijkstra(vertices, graph, src, dest):
        
    distance = [math.inf]*(vertices+1)
    parent= [-1]*(vertices+1)
    visited=[False] * (vertices+1)
    min_heap=[]
    heappush(min_heap, (0, src))
    distance[src]=0
    while min_heap:
        curdist, currnode = heappop(min_heap)
        if currnode == dest:
            print(curdist)
            return curdist

        if visited[currnode] is False:
            visited[currnode] = True
            

            for nbr in range(1, vertices+1):
                if graph[currnode][nbr] != -1 and curdist+graph[currnode][nbr] < distance[nbr]:
                    distance[nbr] = curdist + graph[currnode][nbr]
                    parent[nbr] = currnode
                    heappush(min_heap, (distance[nbr], nbr))
    return distance[dest] if distance[dest] != math.inf else -1

        
dijkstra(vertices, graph, 1, 4)


# 4
# 5
# 1 2 2
# 1 3 9
# 1 4 14
# 2 3 9
# 3 4 2

# ans= 11

