class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(pos,K):
            if K==0 or pos<0:
                return 0
            ret=probe(pos-1,K)
            acc=0
            for i in range(min(K,len(piles[pos]))):
                acc+=piles[pos][i]
                ret=max(ret,acc+probe(pos-1,K-i-1))
            return ret
        return probe(len(piles)-1,k)

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        prefix=[[0]*(len(item)+1) for item in piles]
        for i in range(len(piles)):
            for j in range(len(piles[i])):
                prefix[i][j]=piles[i][j]+prefix[i][j-1]
        dp=[[-1]*(k+1) for item in piles]
        for i in range(min(k,len(piles[0]))):
            dp[0][i+1]=prefix[0][i]
        dp[0][0]=0
        for i in range(1,len(piles)):
            dp[i][0]=0
            for j in range(k+1):
                dp[i][j]=dp[i-1][j]
                for idx in range(len(piles[i])):
                    if j-idx-1<0:
                        break
                    dp[i][j]=max(dp[i-1][j-idx-1]+prefix[i][idx],dp[i][j])
        return dp[-1][-1]