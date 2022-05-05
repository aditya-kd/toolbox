def dfs(node, parent, visited, graph):
    visited[node] = True
    for nbr in graph[node]:
        if visited[nbr] is not True:
            dfs(nbr, node, visited, graph)
        elif nbr != parent:
            print(node,'--->', nbr)

def print_backedges(edges, num_vertices, num_edges):
    graph = dict()
    for i in range(num_vertices):
        graph[i] = list()
    for edge in edges:
        u, v= edge[0], edge[1]
        graph[u].append(v)
        graph[v].append(u)

    visited = [False]*(num_vertices)
    dfs(0, -1, visited, graph)
if __name__ == '__main__':
    num_vertices = int(input())
    num_edges =int(input())
    edges= []
    for i in range( num_edges):
        u, v= tuple(map(int,input().split()))
        edges.append([u,v])

    print_backedges(edges, num_vertices, num_edges)
