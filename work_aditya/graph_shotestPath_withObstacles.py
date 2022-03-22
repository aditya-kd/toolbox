from collections import deque
def shortestPath(grid, obstacles: int) -> int:
        rows =len(grid)
        cols= len(grid[0])
        queue = deque()
        state= (0,0,obstacles)
        queue.append((state, 0))
        visited= set([state])
        
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        while queue:
            state, steps= queue.popleft()
            row, col, curr= state
            if row==rows-1 and col ==cols-1:
                return steps
            for direction in directions:
                new_row, new_col =row+direction[0], col+direction[1]
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col>= cols:
                    continue
                new_obs= curr- grid[new_row][new_col]
                new_state= (new_row, new_col, new_obs)
                if new_obs >=0 and new_state not in visited:
                    queue.append((new_state, steps+1))
                    visited.add(new_state)
            
            
        return -1