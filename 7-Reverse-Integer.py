class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        up_bound=0x7fffffff
        low_bound=~up_bound
        if x<0:
            ret=-int(s[:0:-1])
        else:
            ret=int(s[::-1])
        if ret<low_bound or ret>up_bound:
            return 0
        return ret