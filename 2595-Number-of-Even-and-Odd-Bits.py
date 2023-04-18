class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ret=[0,0]
        cur=0
        while n:
            if n&1:
                ret[cur]+=1
            cur=1-cur
            n=n>>1
        return ret
