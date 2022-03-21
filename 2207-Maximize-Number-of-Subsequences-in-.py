class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        dp=[[0,0,1] for _ in range(3)]
        for i in range(len(text)):
            cur=text[i]
            for j in range(len(pattern)-1,-1,-1):
                dp[j][j]=max(dp[j][j],dp[-1][j]+dp[-1][j-1])
            for j in range(len(pattern)-1,-1,-1):
                if pattern[j]==cur:
                    dp[j][j]+=dp[j][j-1]
                    dp[1-j][j]+=dp[1-j][j-1]
                    dp[-1][j]+=dp[-1][j-1]
            for j in range(len(pattern)-1,-1,-1):
                dp[j][j]=max(dp[j][j],dp[-1][j]+dp[-1][j-1])
        return max(dp[0][1],dp[1][1])
                    