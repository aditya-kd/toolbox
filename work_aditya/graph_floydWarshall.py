def acceptGraph(v, e):
    
    graph=[[-1]*(v+1) for i in range(v+1)]
    for i in range(e):
        src,dest, wt= tuple(map(int, input().split()))
        graph[src][dest]=wt
        graph[dest][src]=wt
    return graph
        
import math
def floydWarshall():
    v= int(input("Vertices:?"))
    e= int(input("Edges:?"))
    graph = acceptGraph(v, e)
    for i in range(v):
        for j in range(v):
            if i==j and graph[i][j] == math.inf:
                graph[i][j] = 0

    for k in range(v):
        for i in range(v):
            for j in range(v):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    
    for line in graph:
        print(line)
    return graph

floydWarshall()





