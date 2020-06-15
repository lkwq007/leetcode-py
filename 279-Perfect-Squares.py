class Solution:
    def numSquares(self, n: int) -> int:
        import math
        count=0
        max_part=int(math.sqrt(n))
        i=1
        while n>0:
            
