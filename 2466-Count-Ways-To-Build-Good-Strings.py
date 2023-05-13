class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        term=10**9+7
        dp=[0]*(high+1)
        ret=0
        dp[0]=1
        for i in range(1,high+1):
            if i-zero>=0:
                dp[i]+=dp[i-zero]
            if i-one>=0:
                dp[i]+=dp[i-one]
            dp[i]%=term
            if i>=low:
                ret+=dp[i]
        return ret%term