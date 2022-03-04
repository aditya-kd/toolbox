def dfs(grid, x, y, m, n):
    if x<0 or y< 0 or x>=m or y>=n or grid[x][y]=='0':
        return
    grid[x][y]='0'
    dfs(grid, x+1, y, m, n)
    dfs(grid, x-1, y, m, n)
    dfs(grid, x,y+1, m,n)
    dfs(grid, x, y-1, m, n)
    
def connectedCells(grid):
    if grid==None:
        return 0
    m=len(grid)
    n=len(grid[0])
    total=0
    for i in range(m):
        for j in range(n):
            total+= ord(grid[i][j]-ord('0'))
            dfs(grid, i,j, m, n)
    return total

