class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        record=[0]*3
        for item in stones:
            record[item%3]+=1
        total0=sum(record)
        # optimally, will not choose to lose
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(lst,acc):
            lst=list(lst)
            total=sum(lst)
            if total==0:
                return (total0%2)==1
            lose=(3-acc)%3
            if total==lst[lose]:
                return False
            ret=False
            for i in range(3):
                if i!=lose and lst[i]>0:
                    lst[i]-=1
                    ret=ret or (not probe(tuple(lst),(acc+i)%3))
                    lst[i]+=1
            return ret
        return probe(tuple(record),0)
            