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