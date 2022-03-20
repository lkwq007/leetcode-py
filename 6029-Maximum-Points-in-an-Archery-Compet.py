import functools
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self.ret=0
        self.lst=[]
        mask=1
        mapping=[0]*12
        for i in range(12):
            mapping[i]=mask
            mask=mask<<1
        @functools.lru_cache(maxsize=None)
        def probe(cur,acc):
            ret=0
            lst=[0]*12
            for i in range(1,12):
                if cur&mapping[i]==0 and acc>aliceArrows[i]:
                    probe(cur|mapping[i],acc-aliceArrows[i]-1)
                if cur&mapping[i]:
                    lst[i]=aliceArrows[i]+1
                    ret+=i
            lst[0]=numArrows-sum(lst)
            if ret>self.ret:
                self.ret=ret
                self.lst=lst
            # self.ret=max(ret,self.ret)
        probe(0,numArrows)
        return self.lst
