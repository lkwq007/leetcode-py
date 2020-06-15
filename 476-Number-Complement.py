class Solution:
    def findComplement(self, num: int) -> int:
        # num is positive
        if num>=1:
            cur=1-num%2
            return cur+(self.findComplement(num>>1)<<1)
        else:
            return 0


x=Solution()
print(x.findComplement(5))
print(x.findComplement(1))
print(x.findComplement(2))