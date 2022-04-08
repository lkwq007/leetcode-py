class Solution:
    def numberOfWays(self, s: str) -> int:
        zero=0
        one=0
        for item in s:
            if item=="0":
                zero+=1
            else:
                one+=1
        acc0=0
        acc1=0
        ret=0
        for item in s:
            if item=="0":
                zero-=1
                acc0+=1
                ret+=acc1*one
            else:
                one-=1
                acc1+=1
                ret+=acc0*zero
        return ret