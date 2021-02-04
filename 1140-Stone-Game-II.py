import functools
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp
        total=len(piles)
        if total<3:
            return sum(piles)
        acc=0
        for i in range(len(piles)):
            piles[i]+=acc
            acc=piles[i]
        @functools.lru_cache(maxsize=None)
        def probe(pos,M):
            if pos+2*M>=total:
                return 0,piles[-1]-piles[pos-1]
            ret=[0,0]
            left=0 if pos==0 else piles[pos-1]
            for i in range(pos,min(pos+2*M,total)):
                offset=i-pos+1
                offset=max(offset,M)
                tmp=probe(i+1,offset)
                if ret[1]<=tmp[0]+piles[i]-left:
                    ret[1]=tmp[0]+piles[i]-left
                    ret[0]=tmp[1]
            return ret
        return probe(0,1)[1]