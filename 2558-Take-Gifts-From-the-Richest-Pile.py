class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import heapq
        from math import sqrt
        heap=[-item for item in gifts]
        heapq.heapify(heap)
        for i in range(k):
            top=-heapq.heappop(heap)
            heapq.heappush(heap,-int(sqrt(top)))
        return -sum(heap)