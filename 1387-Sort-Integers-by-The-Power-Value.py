class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # even x=x>>1
        # odd x=2*x+x+1, next: x+(x+1)>>1
        dp=[0]*(3*hi+2)
        for i in range(2,hi+1):
            tmp=i
            while tmp>1:
                if tmp%2:
