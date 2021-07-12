import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        limit=10**6
        self.minheap=[limit]
        self.maxheap=[limit]
        self.total=0
        self.median=0

    def addNum(self, num: int) -> None:
        if self.total==0:
            self.median=num
        elif self.total%2:
            # odd num
            prev=-heapq.heappop(self.maxheap)
            next=heapq.heappop(self.minheap)
            lst=[num,prev,next,self.median]
            lst.sort()
            self.median=(lst[1]+lst[2])/2
            heapq.heappush(self.maxheap,-lst[0])
            heapq.heappush(self.maxheap,-lst[1])
            heapq.heappush(self.minheap,lst[2])
            heapq.heappush(self.minheap,lst[3])
        else:
            # even num
            prev=-heapq.heappop(self.maxheap)
            next=heapq.heappop(self.minheap)
            lst=[num,prev,next]
            lst.sort()
            self.median=lst[1]
            heapq.heappush(self.maxheap,-lst[0])
            heapq.heappush(self.minheap,lst[2])
        self.total+=1

    def findMedian(self) -> float:
        return self.median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()