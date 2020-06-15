class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left=1
        right=x
        while left<right:
            middle=left+(right-left)//2
            if middle*middle>x:
                right=middle
            elif middle*middle<x:
                left=middle+1 
            else:
                return middle
        return left-1