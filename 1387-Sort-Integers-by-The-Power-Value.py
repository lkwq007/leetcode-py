class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # even x=x>>1
        # odd x=2*x+x+1, next: x+(x+1)>>1
        dp=[0]*(3*hi+6)
        def power(x):
            if dp[x]==0 and x!=1:
                if x%2:
                    ret=power(3*x+1)
                else:
                    ret=power(x//2)
                dp[x]=1+ret
                return ret
            return dp[x]
        ret=list(range(lo,hi+1))
        for i in range(2,hi+1):
            tmp=power(i)
        ret.sort(lambda x: dp[x])
        return ret[k-1]
