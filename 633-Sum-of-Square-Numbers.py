from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        base=int(sqrt(c))
        if base*base==c:
            return True
        for i in range(1,base):
            rest=c-i*i
            tmp=int(sqrt(rest))
            if tmp*tmp==rest:
                return True
        return False