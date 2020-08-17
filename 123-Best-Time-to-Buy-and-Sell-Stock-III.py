import functools
class Solution:
    # TLE
    def maxProfit(self, prices: List[int]) -> int:
        start=0
        end=len(prices)-1
        while start<len(prices)-1 and prices[start]>=prices[start+1]:
            start+=1
        while end>0 and prices[end]<=prices[end-1]:
            end-=1
        if end<=start:
            return 0
        # buy once
        @functools.lru_cache(maxsize=None)
        def seg_min(i,j):
            if i==j:
                return prices[i]
            else:
                return min(seg_min(i,j-1),prices[j])
        @functools.lru_cache(maxsize=None)
        def seg_max(i,j):
            if i==j:
                return prices[i]
            else:
                return max(seg_max(i,j-1),prices[j])
        # once
        once=0
        # end=len(prices)-1
        for i in range(start,end):
            once=max(once,seg_max(i+1,end)-seg_min(start,i))
        if end-start+1<4:
            return once
        # twice
        def probe(i,j):
            ret=0
            for idx in range(i,j):
                ret=max(ret,seg_max(idx+1,j)-seg_min(i,idx))
            return ret
        twice=0
        for i in range(start+1,end-1):
            twice=max(twice,probe(start,i)+probe(i+1,end))
        return max(once,twice)