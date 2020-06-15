class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m==n:
            return m
        def helper(a,b):
            if b>a:
                return a&b&(helper(a>>1,b>>1)<<1)
            else:
                return b
        return helper(m,n)

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        return m&n&(self.rangeBitwiseAnd(m>>1,n>>1)<<1) if n>m else n

x=Solution()
print(x.rangeBitwiseAnd(2,3))

