class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret=x^y
        cnt=0
        while ret>0:
            cnt+=ret&1
            ret=ret>>1
        return cnt