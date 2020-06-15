class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry=0
        cur=1
        ret=0
        for i in range(0,63):
            a_=(a>>i)&1
            b_=(b>>i)&1
            s=a_^b_^carry
            carry=(a_&b_)|(a_&carry)|(b_&carry)
            ret=ret|(s<<i)
        return ret
x=Solution()
print(x.getSum(12,-80))