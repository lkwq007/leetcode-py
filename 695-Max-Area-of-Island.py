class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h=len(grid)
        w=len(grid[0])
        self.acc=0
        self.ret=0
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(y0,x0):
            grid[y0][x0]=-1
            self.acc+=1
            self.ret=max(self.ret,self.acc)
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=x1<w and 0<=y1<h and grid[y1][x1]==1:
                    dfs(y1,x1)
        for y in range(h):
            for x in range(w):
                if grid[y][x]==1:
                    self.acc=0
                    dfs(y,x)
        return self.ret