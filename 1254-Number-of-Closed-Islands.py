class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # remove open island
        h=len(grid)
        w=len(grid[0])
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(y0,x0):
            grid[y0][x0]=-1
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=y1<h and 0<=x1<w and grid[y1][x1]==0:
                    dfs(y1,x1)
        # border
        for x in range(w):
            if grid[0][x]==0:
                dfs(0,x)
            if grid[h-1][x]==0:
                dfs(h-1,x)
        for y in range(h):
            if grid[y][0]==0:
                dfs(y,0)
            if grid[y][w-1]==0:
                dfs(y,w-1)
        ret=0
        for y in range(1,h-1):
            for x in range(1,w-1):
                if grid[y][x]==0:
                    ret+=1
                    dfs(y,x)
        return ret