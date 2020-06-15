class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        def pow_(base,p):
            if p==1:
                return base
            if p==0:
                return 1
            tmp=pow_(base,p//2)
            if p%2==1:
                return tmp*tmp*base
            else:
                return tmp*tmp
        ret=pow_(x,abs(n))
        ret=1/ret if n<0 else ret
        return ret
