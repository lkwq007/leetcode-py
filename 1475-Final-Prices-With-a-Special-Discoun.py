class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        if len(prices)<2:
            return prices
        discount=[0]*len(prices)
        stack=[0]
        for idx in range(len(prices)-1,-1,-1):
            cur=prices[idx]
            while stack and stack[-1]>cur:
                stack.pop()
            discount[idx]=cur-stack[-1]
            stack.append(cur)
        return discount

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        if len(prices)<2:
            return prices
        ret=[0]*len(prices)
        stack=[0]
        for idx in range(len(prices)-1,-1,-1):
            while stack and stack[-1]>prices[idx]:
                stack.pop()
            ret[idx]=prices[idx]-stack[-1]
            stack.append(prices[idx])
        return ret