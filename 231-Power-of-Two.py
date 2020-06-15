class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n&(n-1))==0

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        if n==1:
            return True
        while n%2==0:
            n=n>>1
        return n==1