class Solution:
    def twoEggDrop(self, n: int) -> int:
        if n<3:
            return n
        import functools
        @functools.lru_cache(None)
        def probe(num,rest):
            if rest==1:
                return num
            if num<3:
                return num
            ret=num
            for i in range(num):
                tmp=1+max(probe(num-i-1,2),probe(i,1))
                ret=min(tmp,ret)
            return ret
        return probe(n,2)
