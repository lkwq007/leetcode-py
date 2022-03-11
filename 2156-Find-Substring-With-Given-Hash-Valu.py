class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        # reverse?
        acc=0
        base=ord("a")-1
        for i in range(k):
            acc*=power
            acc+=ord(s[-i-1])-base
            acc%=modulo
        ret=len(s)
        if acc==hashValue:
            ret=len(s)-k
        lst=[1]*(len(k)+1)
        for i in range(1,k+1):
            lst[i]=(lst[i-1]*power)%modulo
        for i in range(len(s)-k-1,-1,-1):
            acc*=power
            acc=acc+ord(s[i])-base-(ord(s[i+k])-base)*lst[k]+modulo
            acc%=modulo
            if acc==hashValue:
                ret=i
        return s[ret:ret+k]