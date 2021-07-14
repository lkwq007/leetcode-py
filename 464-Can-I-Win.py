class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if sum(range(1,maxChoosableInteger+1))<desiredTotal:
            return False
        import functools
        total=(1<<maxChoosableInteger)-1
        @functools.lru_cache(maxsize=None)
        def probe(acc,mask):
            if mask==total:
                return False
            cur=1
            flag=False
            for i in range(1,maxChoosableInteger+1):
                if cur&mask==0:
                    if i>=acc:
                        return True
                    elif not probe(acc-i,cur|mask):
                        return True
                cur=cur<<1
            return False
        return probe(desiredTotal,0)