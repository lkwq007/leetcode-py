from math import ceil
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        template=[-1]*(len(dist)+1)
        dp=[template[:] for _ in range(len(dist)+1)]
        dp[0][0]=0
        for i in range(len(dist)):
            dp[0][i+1]=ceil(dp[0][i]-1e-9)+dist[i]/speed
            dp[i+1][0]=0
        if dp[0][-1]<=hoursBefore:
            return 0
        for i in range(1,len(dist)+1):
            for j in range(len(dist)):
                dp[i][j+1]=min(ceil(dp[i][j]-1e-9)+dist[j]/speed,dp[i-1][j]+dist[j]/speed)
            # print(dp)
            if dp[i][-1]<=hoursBefore:
                return i
        return -1
