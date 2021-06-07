class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        template=[-1]*(len(stations)+1)
        dp=[template[:] for _ in range(len(stations)+1)]
        dp[0][0]=startFuel
        last=0
        for i in range(len(stations)):
            cur=stations[i][0]
            dp[0][i+1]=dp[0][i]-(cur-last)
            last=cur
            if dp[0][i+1]<0:
                break
        for i in range(1,len(stations)+1):
            last=0
            for j in range(len(stations)):
                diff=stations[j][0]-last
                dp[i][j+1]=max(dp[i][j]-diff,dp[i-1][j]+stations[j])
                last=stations[j][0]