class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        lenA=len(A)
        lenB=len(B)
        if lenA<1 or lenB<1:
            return 0
        template=[0]*(lenB+1)
        dp=[template[:] for i in range(0,lenA+1)]
        for i in range(1,lenA+1):
            for j in range(1,lenB+1):
                cur=1 if A[i-1]==B[j-1] else 0
                dp[i][j]=max(dp[i-1][j-1]+cur,dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

