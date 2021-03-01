class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2147483648 and divisor==-1:
            return 2147483647
        if dividend==0 or divisor==1:
            return dividend
        sign=lambda x:(0 if x>0 else 1)
        s1=sign(dividend)
        s2=sign(divisor)
        s=s1^s2
        dividend=abs(dividend)
        divisor=abs(divisor)
        if divisor>dividend:
            return 0
        cur=divisor
        cnt=1
        while cur<dividend:
            cur=cur<<1
            cnt=cnt<<1
        ret=0
        while cur>=divisor:
            if dividend>=cur:
                dividend-=cur
                ret+=cnt
            cur=cur>>1
            cnt=cnt>>1
        return ret if s==0 else -ret


import math
class Solution:
    # not a solution
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2147483648 and divisor==-1:
            return 2147483647
        ret=dividend/divisor
        if ret<0:
            return math.ceil(ret)
        return math.floor(ret)