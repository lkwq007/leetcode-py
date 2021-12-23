class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ret=0
        acc=0
        for i in range(len(prices)):
            if i>0 and prices[i-1]-1==prices[i]:
                acc+=1
            else:
                acc=1
            ret+=acc
        return ret