class Solution:
    def numberOfMatches(self, n: int) -> int:
        ret=0
        while n>1:
            if n&1:
                n=n//2+1
                ret+=n-1
            else:
                n=n//2
                ret+=n
        return ret

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1