class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # at most 20 cells
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        self.ret=0
        h=len(grid)
        w=len(grid[0])
        total=0
        start=None
        end=None
        for y in range(h):
            for x in range(w):
                if grid[y][x]==0:
                    total+=1
                elif grid[y][x]==1:
                    start=(y,x)
                elif grid[y][x]==2:
                    end=(y,x)
        if start is None or end is None:
            return 0
        def dfs(y0,x0,acc):
            tmp=grid[y0][x0]
            grid[y0][x0]=3
            for y_offset,x_offset in direction:
                y1=y0+y_offset
                x1=x0+x_offset
                if 0<=y1<h and 0<=x1<w:
                    if acc==total and grid[y1][x1]==2:
                        self.ret+=1
                    elif grid[y1][x1]==0:
                        dfs(y1,x1,acc+1)
            grid[y0][x0]=tmp
        dfs(start[0],start[1],0)
        return self.ret