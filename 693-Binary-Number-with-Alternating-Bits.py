class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last=~(n&1)
        # positive
        while n>0:
            cur=n&1
            if (cur^last)&1==0:
                return False
            last=cur
            n=n>>1
        return True