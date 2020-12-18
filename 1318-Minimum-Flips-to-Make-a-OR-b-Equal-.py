class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        mask=1
        ret=0
        while (a|b|c)>0:
            if c&1:
                if (a&1)+(b&1)==0:
                    ret+=1
            else:
                ret+=(a&1)+(b&1)
            a=a>>1
            b=b>>1
            c=c>>1
        return ret