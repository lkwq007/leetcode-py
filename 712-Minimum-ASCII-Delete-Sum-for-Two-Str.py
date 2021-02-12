class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        template=[0]*(len(s2)+1)
        dp=[template[:] for _ in range(len(s1)+1)]
        ret=0
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=max(dp[i-1][j-1]+1,dp[i][j-1],dp[i-1][j])
                else:
                    dp[i][j]=max(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
                ret=max(ret,dp[i][j])
        return ret