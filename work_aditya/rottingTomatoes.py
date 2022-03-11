class Node:
    def __inti__(self, x, y, time):
        self.x=x
        self.y=y
        self.time=time
        
def solve(grid):
    rows= len(grid)
    cols=len(grid[0])
