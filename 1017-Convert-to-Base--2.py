class Solution:
    def baseNeg2(self, N: int) -> str:
        if N==0:
            return "0"
        x=N
        mask=1
        ret=""
        while x!=0:
            if abs(x)&1:
                ret="1"+ret
                if x<0:
                    x-=1
            else:
                ret="0"+ret
            x=-(x//2)
        return ret
