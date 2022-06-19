class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        record={}
        for h,w,p in prices:
            record[(h,w)]=p
        import functools
        @functools.lru_cache(None)
        def probe(h,w):
            if (h,w) in record:
                ret=record[(h,w)]
            else:
                ret=0
            for i in range(1,h//2+1):
                ret=max(ret,probe(i,w)+probe(h-i,w))
            for i in range(1,w//2+1):
                ret=max(ret,probe(h,i)+probe(h,w-i))
            return ret
        return probe(m,n)
