class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val=0
        acc=0
        total=len(prices)
        for idx in range(1,total):
            diff=prices[idx]-prices[idx-1]
            acc=max(0,acc+diff)
            max_val=max(acc,max_val)
        return max_val
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val=prices[0]
        ret=0
        for i in range(1,len(prices)):
            ret=max(prices[i]-min_val,ret)
            min_val=min(prices[i],min_val)
        return ret