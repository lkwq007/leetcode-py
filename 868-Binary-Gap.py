class Solution:
    def binaryGap(self, n: int) -> int:
        ret=0
        cnt=-32
        x=n
        while x>0:
            if x&1:
                ret=max(ret,cnt)
                cnt=1
            else:
                cnt+=1
            x=x>>1
        return ret