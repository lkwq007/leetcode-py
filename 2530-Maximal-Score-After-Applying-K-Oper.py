class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ret=0
        import heapq
        heap=[-item for item in nums]
        heapq.heapify(heap)
        for i in range(k):
            top=-heapq.heappop(heap)
            ret+=top
            top=(top+2)//3
            heapq.heappush(heap,-top)
        return ret