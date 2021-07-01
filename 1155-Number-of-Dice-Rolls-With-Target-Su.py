class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target<d or d*f<target:
            return 0
        import functools
        term=10**9+7
        @functools.lru_cache(maxsize=None)
        def probe(total,idx):
            if idx==d:
                return 1 if total==0 else 0
            if total<=0:
                return 0
            ret=0
            for i in range(1,f+1):
                ret+=probe(total-i,idx+1)
                ret%=term
        