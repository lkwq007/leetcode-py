class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        stack=self.stack
        cnt=1
        while stack:
            if stack[-1][0]>price:
                break
            else:
                tmp=stack.pop()
                cnt+=tmp[1]
        stack.append([price,cnt])
        return cnt

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)