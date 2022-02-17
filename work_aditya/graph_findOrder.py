def findOrder(self, numCourses, prerequisites) :
        adjLists=[[] for i in range(numCourses)]
        indegree=[0]*numCourses
        for edge in prerequisites:
            v1=edge[1]
            v2= edge[0]
            adjLists[v1].append(v2)
            indegree[v2]+=1
    
        sources=[]
        for i in range(0, numCourses):
            if indegree[i]==0 :
                sources.append(i)
    
        topoorder=[]
        while len(sources)>0:
            course= sources[-1]
            sources.pop()
            topoorder.append(course)

            for neigh in adjLists[course]:
                indegree[neigh]-=1
                if indegree[neigh] ==0:
                    sources.append(neigh)
            
        if len(topoorder) < numCourses:
            topoorder=[]
        return topoorder