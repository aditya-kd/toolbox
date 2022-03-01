#include<bits/stdc++.h>
using namespace std;

int n, m;
queue<int> q;
int go_immediately_to[110], dist[110];
bool vis[110];
bool isValid(int node)
{
    if(node < 1 || node > 100 || vis[node])
        return false;
    else
        return true;
}
int BFS(int source)
{
    memset(vis, 0, sizeof(vis));
    while(!q.empty())
        q.pop();

    vis[source] = 1;
    q.push(source);
    dist[source] = 0;
    while(!q.empty())
    {
        int current_node = q.front();
        q.pop();
        for(int i = 1; i<=6; i++)
        {
            int next_node = go_immediately_to[current_node+i];
            if(isValid(next_node))
            {
                q.push(next_node);
                vis[next_node] = 1;
                dist[next_node] = dist[current_node]+1;
            }
        }
    }
    if(!vis[100])
        return -1;
    else
        return dist[100];
}
int main()
{
    int i, j, cs, t, u, v;
    cin >> t;
    for(cs = 1; cs<=t; cs++)
    {
        cin >> n;

        for(i = 1; i<=100; i++)
            go_immediately_to[i] = i;

        for(i = 1; i<=n; i++)
        {
            cin >> u >> v;
            go_immediately_to[u] = v;
        }

        cin >> m;

        for(i = 1; i<=m; i++)
        {
            cin >> u >> v;
            go_immediately_to[u] = v;
        }

        cout << BFS(1) << endl;
    }

}


# # # import sys
# # # def snakes_ladder(dist):# 1 testcase passing only
# # #     ls=[1,2,3,4,5,6]
# # #     chances=0
# # #     dist-=1
# # #     while dist>0:9
# # #         for i in range(len(ls)-1, -1, -1):
# # #             if ls[i]<=dist:
# # #                 dist-=ls[i]
# # #                 print(ls[i],dist)
# # #                 chances+=1
# # #                 break
# # #             if dist==0:
# # #                 break
# # #     if chances==0:
# # #         return -1
# # #     else: return chances
# # # def quickestWayUp(ladders, snakes):
# # #     # Write your code here
# # #     maxLadder=0
# # #     maxDist=-sys.maxsize
# # #     for item in ladders:
# # #         if item[1]>maxDist:
# # #             maxLadder=item
# # #             maxDist=maxLadder[1]
# # #     print(maxLadder)
# # #     chances_ladder=snakes_ladder(maxLadder[0])
# # #     chances_finish=snakes_ladder(100-maxLadder[1])
# # #     print(chances_ladder)
# # #     print(chances_finish)
# # #     print('Answer',chances_ladder+chances_finish)
# # #     return chances_ladder+chances_finish
    
    




# # Python3 program to find minimum number
# # of dice throws required to reach last
# # cell from first cell of a given
# # snake and ladder board

# # An entry in queue used in BFS
# class QueueEntry(object):
# 	def __init__(self, v = 0, dist = 0):
# 		self.v = v
# 		self.dist = dist

# '''This function returns minimum number of
# dice throws required to. Reach last cell
# from 0'th cell in a snake and ladder game.
# move[] is an array of size N where N is
# no. of cells on board. If there is no
# snake or ladder from cell i, then move[i]
# is -1. Otherwise move[i] contains cell to
# which snake or ladder at i takes to.'''
# def getMinDiceThrows(move, N):
	
# 	# The graph has N vertices. Mark all
# 	# the vertices as not visited
# 	visited = [False] * N

# 	# Create a queue for BFS
# 	queue = []

# 	# Mark the node 0 as visited and enqueue it
# 	visited[0] = True

# 	# Distance of 0't vertex is also 0
# 	# Enqueue 0'th vertex
# 	queue.append(QueueEntry(0, 0))

# 	# Do a BFS starting from vertex at index 0
# 	qe = QueueEntry() # A queue entry (qe)
# 	while queue:
# 		qe = queue.pop(0)
# 		v = qe.v # Vertex no. of queue entry

# 		# If front vertex is the destination
# 		# vertex, we are done
# 		if v == N - 1:
# 			break

# 		# Otherwise dequeue the front vertex
# 		# and enqueue its adjacent vertices
# 		# (or cell numbers reachable through
# 		# a dice throw)
# 		j = v + 1
# 		while j <= v + 6 and j < N:
		
# 			# If this cell is already visited,
# 			# then ignore
# 			if visited[j] is False:
				
# 				# Otherwise calculate its
# 				# distance and mark it
# 				# as visited
# 				a = QueueEntry()
# 				a.dist = qe.dist + 1
# 				visited[j] = True

# 				# Check if there a snake or ladder
# 				# at 'j' then tail of snake or top
# 				# of ladder become the adjacent of 'i'
# 				a.v = move[j] if move[j] != -1 else j

# 				queue.append(a)

# 			j += 1

# 	# We reach here when 'qe' has last vertex
# 	# return the distance of vertex in 'qe
# 	return qe.dist

# # driver code
# N = 300
# moves = [-1] * N

# # Ladders
# moves[2] = 21
# moves[4] = 7
# moves[10] = 25
# moves[19] = 28

# # Snakes
# moves[26] = 0
# moves[20] = 8
# moves[16] = 3
# moves[18] = 6
# print(getMinDiceThrows(moves, N))
# # print("Min Dice throws required is {0}".
# # 	format(getMinDiceThrows(moves, N)))

# # This code is contributed by Ajitesh Pathak



def isSubsetSum (self, N, arr, summ):
        # code here
        dp = [[-1]*(summ+1) for i in range(N+1)]
        
        def helper(N,summ,arr,dp):
            if dp[N][summ]!=-1:
                return dp[N][summ]
            if summ== 0:
                dp[N][summ] = True
                return dp[N][summ]
            if N == 0:
                dp[N][summ] = False
                return dp[N][summ]
            if arr[N-1]>summ:
                dp[N][summ] = helper(N-1,summ,arr,dp)
                return dp[N][summ]
            dp[N][summ] = helper(N-1,summ,arr,dp) or helper(N-1,summ-arr[N-1],arr,dp)
            return dp[N][summ]
        return helper(N,summ,arr,dp

