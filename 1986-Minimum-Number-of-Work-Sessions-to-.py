class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        mask=1
        mapping=[0]*len(tasks)
        for i in range(len(tasks)):
            mapping[i]=mask
            mask=mask<<1
        if sum(tasks)<=sessionTime:
            return 1
        import functools
        @functools.lru_cache(None)
        def probe(acc,val):
            if acc==(mask-1):
                return 1 if val>0 else 0
            ret=len(tasks)
            for i in range(len(mapping)):
                if (acc&mapping[i])==0:
                    if tasks[i]+val<=sessionTime:
                        ret=min(ret,probe(acc|mapping[i],val+tasks[i]))
                    else:
                        ret=min(ret,1+probe(acc|mapping[i],tasks[i]))
            return ret
        return probe(0,0)