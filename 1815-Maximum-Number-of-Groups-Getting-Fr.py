class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        mapping=[0]*len(groups)
        mask=1
        for i in range(len(mapping)):
            mapping[i]=mask
            mask=mask<<1
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(acc):
            ret=0
            cnt=0
            for i in range(len(mapping)):
                if acc&mapping[i]:
                    cnt+=groups[i]
            for i in range(len(mapping)):
                if acc&mapping[i]==0:
                    rest=(batchSize-(cnt%batchSize))%batchSize
                    ret=max(ret,probe(acc|mapping[i])+(1 if rest==0 else 0))
            return ret
        return probe(0)