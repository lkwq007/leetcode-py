class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n<2:
            return 10**n
        dp=[0]*(n+1)
        dp[1]=10
        dp[2]=9*9
        for idx in range(3,min(n+1,11)):
            dp[idx]=dp[idx-1]*(10-idx+1)
        return sum(dp)
