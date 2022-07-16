import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.heap=[]
        self.inf_cur=1

    def popSmallest(self) -> int:
        if self.heap:
            top=heapq.heappop(self.heap)
            while self.heap and self.heap[0]==top:
                heapq.heappop(self.heap)
        else:
            top=self.inf_cur
            self.inf_cur+=1
        return top
    def addBack(self, num: int) -> None:
        if num<self.inf_cur:
            heapq.heappush(self.heap,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)