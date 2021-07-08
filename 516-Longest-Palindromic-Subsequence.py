class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        total=len(s)
        template=[0]*(total+1)
        dp=[template[:] for _ in range(total+1)]
        for i in range(total):
            for j in range(i+1):
                if i==j:
                    dp[i][j]=1
        ret=1
        for i in range(total):
            for j in range(i-1,-1,-1):
                if s[i]==s[j]:
                    dp[j][i]=max(dp[j+1][i-1]+2,dp[j][i])
                else:
                    dp[j][i]=max(dp[j][i-1],dp[j+1][i-1],dp[j+1][i],dp[j][i])
                ret=max(ret,dp[j][i])
        # print(dp)
        return ret