class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp=[0]*(len(stoneValue)+1)
        dp[-2]=stoneValue[-1]
        # dp as score diff
        for i in range(len(stoneValue)-2,-1,-1):
            acc=stoneValue[i]
            dp[i]=acc-dp[i+1]
            for j in range(i+1,min(len(stoneValue),i+3)):
                acc+=stoneValue[j]
                dp[i]=max(dp[i],acc-dp[j+1])
        if dp[0]<0:
            return "Bob"
        elif dp[0]>0:
            return "Alice"
        return "Tie"