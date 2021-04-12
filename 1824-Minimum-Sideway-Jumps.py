class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        template=[len(obstacles)]*(len(obstacles))
        template[-1]=0
        dp=[template[:] for _ in range(3)]
        dp[1][0]=0
        for i in range(1,len(obstacles)):
            for j in range(3):
                if obstacles[i]-1!=j:
                    dp[j][i]=min(dp[j][i-1],dp[(j+1)%3][i-1]+1,dp[(j+2)%3][i-1]+1)
            for j in range(3):
                if obstacles[i-1]-1==j:
                    dp[j][i]=min(dp[(j+1)%3][i]+1,dp[(j+2)%3][i]+1)
        return min(map(lambda x:x[-1],dp))

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        template=[0]*(len(obstacles))
        dp=[template[:] for _ in range(3)]
        dp[1][0]=0
        dp[0][0]=1
        dp[2][0]=1
        for i in range(1,len(obstacles)):
            for j in range(3):
                if obstacles[i]-1==j or obstacles[i-1]-1==j:
                    dp[j][i]=len(obstacles)
                else:
                    dp[j][i]=min(dp[j][i-1],dp[(j+1)%3][i-1]+1,dp[(j+2)%3][i-1]+1)
        return min(map(lambda x:x[-1],dp))