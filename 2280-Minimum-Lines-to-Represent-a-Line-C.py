class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        last=None
        ret=0
        for i in range(1,len(stockPrices)):
            if last is None:
                ret+=1
            else:
                x1,y1=stockPrices[i]
                x,y=stockPrices[i-1]
                x0,y0=last
                if (y1-y)*(x-x0)!=(y-y0)*(x1-x):
                    ret+=1
            last=stockPrices[i-1]
        return ret