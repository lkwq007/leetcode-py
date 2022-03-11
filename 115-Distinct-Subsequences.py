class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s)<len(t):
            return 0
        dp=[0]*len(t)
        for i in range(len(s)):
            for j in range(len(t)-1,-1,-1):
                if s[i]==t[j]:
                    dp[j]=dp[j]+(dp[j-1] if j>0 else 1)
        return dp[-1]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s)<len(t):
            return 0
        template=[0]*(len(t))
        dp=[template[:] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]==t[j]:
                    dp[i][j]=dp[i-1][j]+(dp[i-1][j-1] if j>0 else 1)
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
