class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        h=len(grid)
        w=len(grid[0])
        last=[0]*w
        for i in range(w):
            last[i]=grid[0][i]
        for y in range(1,h):
            dp=[999999999]*w
            for x in range(w):
                for z in range(w):
                    dp[x]=min(dp[x],last[z]+moveCost[grid[y-1][z]][x]+grid[y][x])
            last=dp
        return min(last)