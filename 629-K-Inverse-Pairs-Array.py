class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # sliding windows?
        template=[0]*(k+1)
        term=10**9+7
        dp=[template[:] for _ in range(n+1)]
        dp[0][0]=1
        for i in range(1,n):
            acc=0
            for j in range(k+1):
                acc+=dp[i-1][j]
                if j-i-1>=0:
                    acc-=dp[i-1][j-i-1]
                dp[i][j]+=acc
                dp[i][j]%=term
        # [print(item) for item in dp]
        return dp[n-1][k]


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        #TLE
        template=[0]*(k+1)
        term=10**9+7
        dp=[template[:] for _ in range(n+1)]
        dp[0][0]=1
        for i in range(1,n):
            for j in range(k+1):
                for idx in range(i+1):
                    if j+idx<=k:
                        dp[i][j+idx]+=dp[i-1][j]
                        dp[i][j+idx]%=term
        # [print(item) for item in dp]
        return dp[n-1][k]