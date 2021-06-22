class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        template=[0]*K
        dp=[template[:] for _ in range(len(A))]
        prefix=A[:]
        acc=0
        for i in range(len(A)):
            acc+=prefix[i]
            prefix[i]=acc
        for i in range(len(A)):
            dp[i][0]=prefix[i]/(i+1)
        for i in range(len(A)):
            for j in range(1,min(K,i+1)):
                for idx in range(i):
                    dp[i][j]=max(dp[i][j],dp[idx][j-1]+(prefix[i]-prefix[idx])/(i-idx))
        return max(dp[-1])