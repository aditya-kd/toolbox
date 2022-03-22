from collections import deque

def shortestPathBinaryMatrix( grid) -> int:
        rows, cols= len(grid), len(grid[0])
        directions= [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
        if grid[0][0]==1 or grid[rows-1][cols-1]==1:
            return -1
        queue= deque()
        queue.append((0,0))
        grid[0][0]=1
        while queue:
            row, col = queue.popleft()
            distance= grid[row][col]
            if row==rows-1 and col==cols-1:
                return distance
            for direction in directions:
                new_row, new_col= row+direction[0], col+direction[1]
                if new_row < 0 or new_row>=rows or new_col<0 or new_col>=cols or grid[new_row][new_col]!=0:
                    continue
                queue.append((new_row, new_col))
                grid[new_row][new_col]=distance+1#we can take a visited array also but uses more space
                
        return -1