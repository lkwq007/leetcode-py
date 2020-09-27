class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        h=len(grid)
        w=len(grid[0])
        if h*w<4:
            return False
        self.timer=1
        template=[0]*w
        tin=[template[:] for _ in range(h)]
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(y0,x0,enter):
            tin[y0][x0]=self.timer
            self.timer+=1
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=x1<w and 0<=y1<h and grid[y1][x1]==grid[y0][x0]:
                    if tin[y1][x1]==0:
                        if dfs(y1,x1,enter):
                            return True
                    else:
                        if tin[y0][x0]-tin[y1][x1]+1>=4:
                            return True
            return False
        for y in range(h):
            for x in range(w):
                if tin[y][x]==0:
                    if dfs(y,x,self.timer):
                        return True
        return False