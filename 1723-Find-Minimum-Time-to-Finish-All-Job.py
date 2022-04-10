class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        if k==len(jobs):
            return max(jobs)
        mapping=jobs[:]
        mask=1
        for i in range(len(mapping)):
            mapping[i]=mask
            mask=mask<<1
        total=sum(jobs)
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(acc,pos):
            if pos==k-1:
                cur=0
                for i in range(len(mapping)):
                    if mapping[i]&acc==0:
                        cur+=jobs[i]
                return cur
            cnt=0
            ret=0
            for i in range(len(mapping)):
                if mapping[i]&acc==0:
                    cnt+=1
                    ret=max(jobs[i],ret)
            if k-pos>=cnt:
                return ret
            ret=total
            for i in range(mask):
                cur=0
                if (acc&i)==acc and (acc&i)!=i:
                    for j in range(len(mapping)):
                        if mapping[j]&i and mapping[j]&acc==0:
                            cur+=jobs[j]
                    ret=min(ret,max(cur,probe(i,pos+1)))
            return ret
        return probe(0,0)