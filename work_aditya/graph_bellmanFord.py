import math


def bellmanFord(n, edges, src):

    dist =[math.inf]*(n)
    dist[src]=0

    for i in range(n-1):
        for node in edges:
            u,v,w= node[0], node[1], node[2]
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    flag=False
    for node in edges:
        u,v,w= node[0], node[1], node[2]
        if dist[u] + w < dist[v]:
            flag=True
            print('Negative Cycle')
            break
    if flag==False:
        for i in dist:
            print(i)

    return dist


vertices= int(input("Vertices"))
e=int(input("Edges"))
edges=[]
for i in range(e):
    u,v,w= tuple(map(int, input().split()))
    edges.append([u,v,w])
print(edges)
print(bellmanFord(vertices, edges, 0))

            
    



