class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        record={}
        ret=0
        for i in range(len(A)):
            record[A[i]]=i
        template=[0]*len(A)
        dp=[template[:] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(i):
                last=A[i]-A[j]
                if last in record and last<A[j]:
                    dp[j][i]=3
                    dp[j][i]=max(dp[j][i],dp[record[last]][j]+1)
                ret=max(ret,dp[j][i])
        return 0 if ret<3 else ret


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        record={}
        ret=0
        for item in A:
            record[item]=1
        dp={}
        for i in range(len(A)):
            for j in range(i):
                last=A[i]-A[j]
                if last in record and last<A[j]:
                    dp[(A[j],A[i])]=3
                dp[(A[j],A[i])]=max(dp.get((A[j],A[i]),2),dp.get((last,A[j]),0)+1)
                ret=max(ret,dp[(A[j],A[i])])
        dp.clear()
        return 0 if ret<3 else ret
