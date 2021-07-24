class Solution:
    def countTriples(self, n: int) -> int:
        # n is quite small, so we can brute force
        ret=0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for k in range(j+1,n+1):
                    if i*i+j*j==k*k:
                        ret+=2
        return ret

import math
class Solution:
    def countTriples(self, n: int) -> int:
        # n is quite small, so we can brute force
        ret=0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                num=i*i+j*j
                part=int(math.sqrt(num))
                if part*part==num and part<=n:
                    ret+=2
        return ret