class Solution:
    def countHousePlacements(self, n: int) -> int:
        term=10**9+7
        template=[0]*n
        dp=[template[:] for _ in range(4)]
        dp[0][0]=1
        dp[1][0]=1
        dp[2][0]=1
        dp[3][0]=1
        # em
        # up
        # down
        # full
        for i in range(1,n):
            dp[0][i]=dp[0][i-1]+dp[1][i-1]+dp[2][i-1]+dp[3][i-1]
            dp[1][i]=dp[0][i-1]+dp[2][i-1]
            dp[2][i]=dp[0][i-1]+dp[1][i-1]
            dp[3][i]=dp[0][i-1]
            for j in range(4):
                dp[j][i]%=term
        return (dp[0][-1]+dp[1][-1]+dp[2][-1]+dp[3][-1])%term

class Solution:
    def countHousePlacements(self, n: int) -> int:
        term=10**9+7
        a,b=1,2
        for i in range(1,n):
            a,b=b%term,(a+b)%term
        return (b*b)%term