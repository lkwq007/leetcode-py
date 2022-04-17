class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ret=0
        while total>0:
            ret+=total//cost2+1
            total-=cost1
        if total==0:
            ret+=1
        return ret