def countChild(node, edgeMap):
    total = edgeMap[node]#already this many nodes are a child of current node
    for child in edgeMap[node]:
        # we also add the children of the children of current node.
        total += countChild(child, edgeMap)
    return total
def evenForest(totalNodes, totalEdges, t_from, t_to):
    edgeMap = {}
    for i in range(1, totalNodes):
        # assigning empty node list to each node
        edgeMap[i] = []

    for i in range(totalEdges):
        u = t_from[i]
        v = t_to[i]
        edgeMap[v].append(u)

    ans = 0
    for node in range(2, len(edgeMap)):
        child = countChild(node, edgeMap)


    