import math

def minkey(vertices, dist, mstset):
    minindex= 0
    minval= math.inf
    for v in range(vertices):
        if dist[v] < minval and mstset[v] == False:
            minval = dist[v]
            minindex= v
    return minindex

def prims(n, graph):
    dist=[math.inf] *(n+1)
    mstset=[False]*(n+1)
    dist[0]=0
    
    for i in range(n):
        u = minkey(n, dist, mstset)
        mstset[u] =True

        for v in range(n):
            if graph[u][v] > 0 and mstset[v] ==False and dist[v] > graph[u][v]:
                dist[v] = graph[u][v]

    return dist

vertices= int(input("Vertices: ?"))
e= int(input("Edges: ?"))
edges=[]
for i in range(e):
    src, dest, wt= tuple(map(int, input().split()))
    edges.append([src, dest,wt])
graph= [ [-1 for i in range(vertices+1)] for j in range(vertices+1)]
for edge in edges:
    src,dest,wt= edge[0], edge[1], edge[2]
    graph[src][dest] = wt

print(prims(vertices, graph))

