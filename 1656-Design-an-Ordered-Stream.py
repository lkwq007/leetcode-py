class OrderedStream:

    def __init__(self, n: int):
        self.buffer=[None]*n
        self.head=0
        self.total=n

    def insert(self, id: int, value: str) -> List[str]:
        self.buffer[id-1]=value
        head=self.head
        while self.head<self.total and self.buffer[self.head] is not None:
            self.head+=1
        return self.buffer[head:self.head]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)