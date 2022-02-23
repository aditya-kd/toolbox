class Solution:
    def backtrack(self, src, dest, graph, partialPath, allPaths):
        if src==dest:
            allPaths.append(partialPath)
            return
        for nbr in graph[src]:
                partialPath.append(nbr)
                self.backtrack(nbr, dest, graph, partialPath, allPaths)
                partialPath.pop()
        return
                
        
    def soln_backtracking(self,graph):
        allPaths=[]
        partialPath=[]
        partialPath.append(0)
        self.backtrack(0, len(graph)-1, graph, partialPath, allPaths)
        return allPaths
    
    def allPathsSourceTarget(self, graph) :
        return self.soln_backtracking(graph)
    
    
        