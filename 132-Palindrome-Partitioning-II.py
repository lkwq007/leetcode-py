import functools
class Solution:
    def minCut(self, s: str) -> int:
        ret=len(s)
        template=[False]*len(s)
        record=[template[:] for _ in range(len(s))]
        for i in range(len(s)):
            record[i][i]=True
            offset=1
            while i-offset>=0 and i+offset<len(s) and s[i-offset]==s[i+offset]:
                record[i-offset][i+offset]=True
                offset+=1
        for i in range(1,len(s)):
            offset=0
            while i-offset-1>=0 and i+offset<len(s) and s[i-offset-1]==s[i+offset]:
                record[i-offset-1][i+offset]=True
                offset+=1
        # @functools.lru_cache(maxsize=None)
        template=[-1]*len(s)
        dp=[template[:] for _ in range(len(s))]
        def probe(start,end):
            if dp[start][end]!=-1:
                return dp[start][end]
            if start==end or record[start][end]:
                return 1
            ret=end-start+1
            for i in range(start,end):
                ret=min(ret,probe(start,i)+probe(i+1,end))
            return ret
        return probe(0,len(s)-1)-1