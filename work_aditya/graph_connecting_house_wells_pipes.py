import math
def buildGraph(n, wells, pipes):
    graph = [[-1 for j in range(n+1)] for i in range(n+1)]
    for pipe in pipes:
        house1 = pipe[0]
        house2=pipe[1]
        cost = pipe[2]
        graph[house1][house2] = cost
        graph[house2][house1]= cost

    for i in range(n):
        graph[0][i+1] = wells[i]
        graph[i+1][0] = wells[i]
    return graph

def find_min(dist, mst_set):
    min_val = math.inf
    index = -1
    for i in range(len(dist)):
        if mst_set[i] == False and min_val < dist[i]:
            min_val= dist[i] 
            index=i
    return index
def solve(n, wells, pipes):
    #mst code
    graph= buildGraph(n, wells, pipes)
    mst_set=[False]*(n+1)
    dist = [math.inf] *(n+1)
    dist[0]= 0
    
    for vertex in range(n+1):
        curr_node = find_min(dist, mst_set)
        mst_set[curr_node] = True
        for vertex in range(n+1):
            if graph[ curr_node][vertex] != -1 and mst_set[vertex] ==False and graph[curr_node][vertex] < dist[vertex]:
                dist[vertex] = graph[curr_node][vertex]
    
    return dist

wells=[1,2,2]
pipes=[[1,2,1],[1,2,2]]
n= 3
print(solve(n, wells, pipes))