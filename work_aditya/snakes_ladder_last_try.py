go_to=[]*101
from collections import deque
def bfs(source):
        bfs=[]
        queue = deque([])
        visited = [False]*101
        dist=[0]*(101)
        #initiate
        queue.append(source)
        visited[source]=True
        dist[source]=0

        while len(queue)!=0:
            currNode= queue.popleft()
            bfs.append(currNode)
            #till here it is standard code to pop node
#calculations from now on.
            for i in range(1, 7):
                next_node= go_to[currNode+i]
                if next_node<1 or next_node>100 or visited[next_node]==True:
                    queue.append(next_node)
                    visited[next_node]=True
                    dist[next_node]=dist[currNode]+1
        if not visited[100]:
            return -1
        else:
            return dist[100]
        

def quickestWayUp(snakes, ladder):
    for i in range(102):
        go_to[i]=i
    for item in snakes:
        go_to[item[0]]=item[1]
    for item in ladder:
        go_to[item[0]]=item[1]
    print(bfs(1))

snakes=[]
ladder=[]
lad_len=int(input())
for i in range(lad_len):
    temp=list(map(int, input().split()))
    ladder.append(temp)
snake_len=int(input())
for i in range(snake_len):
    temp=list(map(int, input().split()))
    snakes.append(temp)
quickestWayUp(snakes, ladder)

    