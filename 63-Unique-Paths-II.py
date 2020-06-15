class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid)<1 or len(obstacleGrid[0])<1:
            return 0
        h=len(obstacleGrid)
        w=len(obstacleGrid[0])
        dp=[0]*h
        dp[-1]=1-obstacleGrid[-1][-1]
        for y in range(h-2,-1,-1):
            if obstacleGrid[y][-1]==1:
                dp[y]=0
            else:
                dp[y]=dp[y+1]
        for x in range(w-2,-1,-1):
            for y in range(h-1,-1,-1):
                if obstacleGrid[y][x]:
                    dp[y]=0
                else:
                    bottom=0 if y+1>=h else dp[y+1]
                    dp[y]+=bottom
        return dp[0]
