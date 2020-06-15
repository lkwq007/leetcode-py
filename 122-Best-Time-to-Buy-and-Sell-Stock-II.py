from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        idx=1
        total=len(prices)
        if total<2:
            return 0
        price=prices[0]
        acc=0
        while idx<total:
            if prices[idx]>prices[idx-1]:
                profit=prices[idx]-price
            else:
                acc+=profit
                profit=0
                price=prices[idx]
            idx+=1
        acc+=prices[idx-1]-price
        return acc

x=Solution()
print(x.maxProfit([3,2,6,5,0,3]))