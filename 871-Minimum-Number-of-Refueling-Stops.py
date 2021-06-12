class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append((target,0))
        template=[-1]*(len(stations)+1)
        dp=[template[:] for _ in range(len(stations)+1)]
        # refuel i times, at station j
        dp[0][0]=startFuel
        last=0
        for i in range(len(stations)):
            loc=stations[i][0]
            dp[0][i+1]=dp[0][i]-(loc-last)
            last=loc
            if dp[0][i+1]<0:
                break
        if dp[0][-1]>=0:
            return 0
        for i in range(len(stations)-1):
            last=0
            for j in range(len(stations)):
                loc=stations[j][0]
                gas=stations[j-1][1] if j>0 else 0
                if dp[i][j]>=0:
                    dp[i+1][j+1]=dp[i][j]-(loc-last)+gas
                dp[i+1][j+1]=max(dp[i+1][j]-(loc-last),dp[i+1][j+1])
                last=loc
            if dp[i+1][-1]>=0:
                return i+1
        return -1
        