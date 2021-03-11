class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[-1]*(amount+1)
        dp[0]=0
        for val in coins:
            dp[val]=1
        for i in range(1,amount+1):
            for val in coins:
                if i-val>=0 and dp[i-val]!=-1:
                    if dp[i]==-1:
                        dp[i]=dp[i-val]+1
                    else:
                        dp[i]=min(dp[i],dp[i-val]+1)
        return dp[amount]