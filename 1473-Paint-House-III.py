class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        template=[-1]*m
        # m*n*target?
        dp=[[template[:] for _ in range(n)] for _ in range(m)]
        cnt=0
        acc=0
        for i in range(m):
            if houses[i]!=0:
                cnt+=1
            else:
                break
        for i in range(n):
            dp[0][i][0]=cost[0][i]
        for i in range(m):
            if houses[i]==0:
                pass
            else:
                pass
        return dp[target][]
