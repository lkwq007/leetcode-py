class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        max_val=n*len(cuts)
        cuts.sort()
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(left,right,li,ri):
            if ri-li<0:
                return 0
            ret=max_val
            for i in range(li,ri+1):
                cut=cuts[i]
                ret=min(ret,probe(left,cut,li,i-1)+probe(cut,right,i+1,ri))
            return ret+right-left
        return probe(0,n,0,len(cuts)-1)