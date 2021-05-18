import heapq
class SeatManager:

    def __init__(self, n: int):
        self.queue=[]
        self.idx=0
        heapq.heapify(self.queue)

    def reserve(self) -> int:
        if len(self.queue)<1:
            self.idx+=1
            return self.idx
        top=heapq.heappop(self.queue)
        return top

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.queue,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)