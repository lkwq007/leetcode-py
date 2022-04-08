import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(key=lambda x:-x)
        if len(nums)<k:
            self.val=None
        else:
            self.val=nums[k-1]
        self.minheap=nums[:k-1]
        heapq.heapify(self.minheap)

    def add(self, val: int) -> int:
        if self.val is None or val>self.val:
            heapq.heappush(self.minheap,val)
            top=heapq.heappop(self.minheap)
            self.val=top
        return self.val



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)