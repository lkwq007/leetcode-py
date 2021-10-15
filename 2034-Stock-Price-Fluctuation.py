import heapq
class StockPrice:

    def __init__(self):
        self.max=None
        self.min=None
        self.cur=None
        self.record={}
        # two heaps
        self.inc_lst=[]
        self.dec_lst=[]

    def update(self, timestamp: int, price: int) -> None:
        if self.cur is None:
            self.cur=timestamp
            # self.min=timestamp
            # self.max=timestamp
            # self.record[timestamp]=price
        self.record[timestamp]=price
        if timestamp>self.cur:
            self.cur=timestamp
        heapq.heappush(self.inc_lst,(price,timestamp))
        heapq.heappush(self.dec_lst,(-price,timestamp))
        while self.inc_lst:
            p,t=self.inc_lst[0]
            if self.record[t]==p:
                break
            heapq.heappop(self.inc_lst)
        while self.dec_lst:
            p,t=self.dec_lst[0]
            if self.record[t]==-p:
                break
            heapq.heappop(self.dec_lst)
        self.max=self.dec_lst[0][1]
        self.min=self.inc_lst[0][1]

    def current(self) -> int:
        return self.record[self.cur]

    def maximum(self) -> int:
        return self.record[self.max]

    def minimum(self) -> int:
        return self.record[self.min]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()