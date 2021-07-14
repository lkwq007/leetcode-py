class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        import functools
        self.ret=max(stones)
        @functools.lru_cache(maxsize=None)
        def probe(idx,acc):
            if idx==len(stones):
                self.ret=min(abs(acc),self.ret)
                return
            probe(idx+1,acc-stones[idx])
            probe(idx+1,acc+stones[idx])
        probe(0,0)
        return self.ret
