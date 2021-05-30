class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        def check(target):
            last=0
            ret=0
            for i in range(len(s)):
                last=0 if s[i]!=target else (last+1)
                ret=max(last,ret)
            return ret
        return check("1")>check("0")