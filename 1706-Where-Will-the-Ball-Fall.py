class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        h=len(grid)
        w=len(grid[0])
        dp=list(range(w))
        for y in range(h-1,-1,-1):
            cur=[-1]*w
            for x in range(w):
                if grid[y][x]==1 and x<w-1 and grid[y][x+1]==1:
                    cur[x]=dp[x+1]
                if grid[y][x]==-1 and x>0 and grid[y][x-1]==-1:
                    cur[x]=dp[x-1]
            dp=cur
        return dp