class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1]*n
        for x in range(0,m):
            for y in range(n-1,-1,-1):
                bottom=0 if y>=n-1 else dp[y+1]
                dp[y]+=bottom
        return dp[0]
