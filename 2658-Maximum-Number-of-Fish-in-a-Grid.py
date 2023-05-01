class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        offset=[(0,1),(0,-1),(1,0),(-1,0)]
        h=len(grid)
        w=len(grid[0])
        def dfs(x,y):
            if grid[x][y]==0:
                return 0
            acc=grid[x][y]
            grid[x][y]=0
            for xo,yo in offset:
                xn=x+xo
                yn=y+yo
                if 0<=xn<h and 0<=yn<w and grid[xn][yn]>0:
                    acc+=dfs(xn,yn)
            return acc
        ret=0
        for i in range(h):
            for j in range(w):
                ret=max(dfs(i,j),ret)
        return ret

