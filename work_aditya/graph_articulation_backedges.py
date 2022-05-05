def dfs(node, parent, vis, dis, low, graph, ap, timer):
    vis[node] = True
    dis[node] = timer
    low[node] = timer
    timer += 1
    child=0
    for nbr in graph[node]:
        if nbr == parent:
            continue
        elif vis[nbr] is not True:
            dfs(nbr, node, vis, dis, low, graph, ap, timer)
            low[node] = min(low[node], low[nbr])

            if low[nbr] >= dis[node]:
                ap.add(node)
            child+=1
        else:
            #backedge
            low[node] = min(low[ node], dis[nbr])
        
    if child >= 2 and parent == -1:
        ap.add(node)
    



def findArtiPoints(edges, vertices):
    visited = [False]*vertices
    discovery_time=[0] *vertices
    lowest_time = [0]*vertices

    articulation_points = set()
    graph= dict()
    timer=0
    for i in range(vertices):
        graph[i] = list()
    
    for edge in edges:
        u, v= edge[0] , edge[1]
        graph[u].append(v)
        graph[v].append(u)
    
    for node in range(vertices):
        if visited[node] == False:
            dfs(node, -1, visited, discovery_time, lowest_time, graph, articulation_points, timer)
    
    return articulation_points

if __name__ =='__main__':
    edges=[[0,1],[0,2],[1,2],[1,3],[3,4],[3,6],[4,5],[5,6]]
    vertices =7
    ans = findArtiPoints(edges, vertices)
    print(ans)