class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        import functools
        total=sum(stones)
        prefix=[0]*(len(stones)+1)
        acc=0
        for i in range(len(stones)):
            acc+=stones[i]
            prefix[i]=acc
        @functools.lru_cache(maxsize=None)
        def probe(start,end,bob=True):
            if start==end:
                return 0,0
            ret0,ret1=probe(start+1,end,not bob)
            ret1+=prefix[end]-prefix[start]
            ret2,ret3=probe(start,end-1,not bob)
            ret3+=prefix[end-1]-prefix[start-1]
            if bob:
                if abs(ret3-ret2)<=abs(ret1-ret0):
                    return ret3,ret2
                else:
                    return ret1,ret0
            elif abs(ret3-ret2)<=abs(ret1-ret0):
                return ret1,ret0
            else:
                return ret3,ret2            
        ret=probe(0,len(stones)-1)
        probe.cache_clear()
        return abs(ret[0]-ret[1])
